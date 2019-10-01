from django.contrib import auth
from django.contrib.auth import login
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView, FormView, RedirectView
from django.contrib.sites.shortcuts import get_current_site

from accounts.forms import RegistrationForm, UserLoginForm
from accounts.models import User
from accounts.tokens import account_activation_token


class RegisterView(CreateView):
    """
    Registration view
    """
    success_url = '/'
    model = User
    form_class = RegistrationForm
    template_name = 'accounts/register.html'

    extra_context = {
        'title': 'Register'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Handle registration post request
        """
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()

            # send email for verification
            send_verification_email(request, user, form)

            return redirect('accounts:login')
        else:
            return render(request, 'accounts/register.html', {'form': form})


class LoginView(FormView):
    """
    Provide the ability to login as a user with an email and password
    """
    success_url = '/'
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    extra_context = {
        'title': 'Login'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    success_url = '/login'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return HttpResponseRedirect(self.success_url)


def activate(request, uidb64, token):
    """
    Provide user the ability to confirm his email.
    :param request: request
    :param uidb64: base 64 encoded user id
    :param token: token
    :return:
    """
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_email_confirmed = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def send_verification_email(request,
                            user,
                            form):
    """
    Send email to newly register user with a link to verify their email
    :param request: request
    :param user: newly registered user
    :param form: registration form
    :return:
    """
    current_site = get_current_site(request)
    mail_subject = 'Confirm Your Email.'
    message = render_to_string('accounts/confirm-email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    to_email = form.cleaned_data.get('email')
    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()

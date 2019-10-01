"""
Token generator module for email verification
"""
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class TokenGenerator(PasswordResetTokenGenerator):
    """
    Token generator for email verification
    """
    def _make_hash_value(self, user, timestamp):
        return (
                 six.text_type(user.pk) + six.text_type(timestamp) +
                 six.text_type(user.is_active)
        )


account_activation_token = TokenGenerator()

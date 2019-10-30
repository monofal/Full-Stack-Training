import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

import { logout } from '../../store/actions/auth';

class Header extends Component {
    constructor(props) {
        super(props);
        this.state = {}
    }

    logout = () => this.props.logout(this.props.history);

    render() {
        const { children, user } = this.props

        return (
            <div>
                <header class="header">

                    <nav class="navbar navbar-expand-lg">
                        <div class="container">
                            <a href="/" class="navbar-brand">
                                <strong>WANT2WORK</strong>
                                <span class="sr-only">Home</span>
                            </a>
                            <button type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
                                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"
                                class="navbar-toggler navbar-toggler-right">Menu<i class="fa fa-bars"></i>
                            </button>
                            <div id="navbarSupportedContent" class="collapse navbar-collapse">

                                {
                                    user.isAuthenticated ?
                                        <ul class="navbar-nav ml-auto">
                                            <li class="nav-item">
                                                <a href="/" class="nav-link">Home <span class="sr-only">(current)</span></a>
                                            </li>
                                            <li class="nav-item">
                                                <a href="" class="nav-link">Dashboard</a>
                                            </li>

                                            <li class="nav-item">
                                                <a href=""
                                                    class="btn navbar-btn btn-outline-light mb-5 mb-lg-0">
                                                    {user.profile.email}
                                                </a>
                                            </li>
                                            <li class="nav-item">
                                                <a onClick={this.logout}
                                                    class="btn navbar-btn btn-outline-light mb-5 mb-lg-0">Logout
                                                </a>
                                            </li>
                                        </ul>
                                        :
                                        <ul class="navbar-nav ml-auto">
                                            <li class="nav-item">
                                                <a href="/register"
                                                    class="btn navbar-btn btn-outline-light mb-5 mb-lg-0">
                                                    Register
                                                 </a>
                                            </li>
                                            {/* <li class="nav-item" style="color: #fff"> */}
                                            <li class="nav-item">
                                                <a href="/login"
                                                    class="btn navbar-btn btn-outline-light mb-5 mb-lg-0">
                                                    <i class="fa fa-sign-in"></i> Login
                                                </a>
                                            </li>
                                        </ul>
                                }
                            </div>
                        </div>
                    </nav>
                </header>


                {children}
            </div>
            // <div>

            //   <Menu className="top">
            //     <Container>
            //       <Menu.Item as={Link} to='/'>Home</Menu.Item>
            //       <Menu.Item as={Link} to='/about'>About</Menu.Item>

            //       {user.isAuthenticated
            //         ? <Menu.Menu position='right'>
            //           <Dropdown item text='My Account'>
            //             <Dropdown.Menu>
            //               <Dropdown.Header
            //                 icon='user'
            //                 content={user.email}
            //               />
            //               <Dropdown.Divider />
            //               <Dropdown.Item as={Link} to='/profile'>Profile</Dropdown.Item>
            //               <Dropdown.Item onClick={this.logout} >Logout</Dropdown.Item>
            //             </Dropdown.Menu>
            //           </Dropdown>
            //         </Menu.Menu>
            //         : <Menu.Menu position='right'>
            //           <Menu.Item as={Link} to='/login'>Login</Menu.Item>
            //           <Menu.Item as={Link} to='/sign-up'>Sign up</Menu.Item>
            //         </Menu.Menu>
            //       }
            //     </Container>
            //   </Menu>
            //   {children}
            // </div>
        )
    }
}

Header.propTypes = {
    user: PropTypes.object,
    children: PropTypes.node,
    logout: PropTypes.func
}

const mapStateToProps = state => ({
    user: state.user
});

export default connect(mapStateToProps, { logout })(withRouter(Header));
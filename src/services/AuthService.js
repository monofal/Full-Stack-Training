
/**
 * Auth Service
 */
import axios from 'axios';
//import { API_URL } from '../config';

const API_URL = "http://127.0.0.1:8000/api"

const AuthService = {
  login: function(email, password) {
    return axios.post(API_URL + '/auth/', { email: email, password: password });
  },
  register: function(data) {
    return axios.post(API_URL + '/register', { data });
  },
  getProfile: function() {
    debugger;
    return axios.get(API_URL + '/current/', { headers: this.authHeader() });
  },
  logout: function () {
    localStorage.removeItem('token');
  },
  getToken: function() {
    return localStorage.getItem('token');
  },
  saveToken: function(token) {
    localStorage.setItem('token', token);
  },
  authHeader: function () {
    return { Authorization: `Bearer ${this.getToken()}` }
  }
}

export default AuthService

import { api } from './api';

interface LoginData {
  username: string;
  password: string;
}
interface RegisterData {
  username: string;
  email: string;
  password: string;
}

export const authService = {
  login: (data: LoginData) => api.post('/token/', data),
  register: (data: RegisterData) => api.post('/register/', data),
  getProfile: () => api.get('/profile/'),
};
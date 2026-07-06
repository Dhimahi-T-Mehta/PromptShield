import axios from "axios";
import { getToken, clearAuth } from "../utils/token";

const api = axios.create({
    baseURL: `${import.meta.env.VITE_API_URL}/api/v1`,
});

// ============================================================
// REQUEST INTERCEPTOR
// ============================================================

api.interceptors.request.use(

    (config) => {

        const token = getToken();

        if (token) {

            config.headers.Authorization = `Bearer ${token}`;

        }

        return config;

    },

    (error) => Promise.reject(error)

);

// ============================================================
// RESPONSE INTERCEPTOR
// ============================================================

api.interceptors.response.use(

    (response) => response,

    (error) => {

        if (error.response?.status === 401) {

            clearAuth();

            if (window.location.pathname !== "/login") {

                window.location.replace("/login");

            }

        }

        return Promise.reject(error);

    }

);

export default api;
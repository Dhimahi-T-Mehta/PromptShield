import {
    createContext,
    useContext,
    useEffect,
    useState,
} from "react";

import {
    loginUser,
} from "../services/auth";

import {
    saveToken,
    getToken,
    saveUser,
    getUser,
    clearAuth,
} from "../utils/token";

import {
    getTokenPayload,
} from "../utils/jwt";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {

    const [user, setUser] = useState(null);

    const [loading, setLoading] = useState(true);

    // Restore session on page refresh
    useEffect(() => {

        const token = getToken();

        const storedUser = getUser();

        if (
            token &&
            storedUser &&
            getTokenPayload(token)
        ) {

            setUser(storedUser);

        } else {

            clearAuth();

        }

        setLoading(false);

    }, []);

    async function login(credentials) {

        const response = await loginUser(credentials);

        const token = response.access_token;

        const payload = getTokenPayload(token);

        if (!payload) {
            throw new Error("Invalid or expired token.");
        }

        const authenticatedUser = {
            username: payload.sub,
            role: payload.role,
            token,
        };

        saveToken(token);

        saveUser(authenticatedUser);

        setUser(authenticatedUser);

        return authenticatedUser;
    }

    function logout() {

    clearAuth();

    setUser(null);

    }

    const value = {

        user,

        login,

        logout,

        loading,

        isAuthenticated: !!user,

    };

    return (

        <AuthContext.Provider value={value}>

            {children}

        </AuthContext.Provider>

    );

}

export function useAuthContext() {

    return useContext(AuthContext);

}
const TOKEN_KEY = "promptshield_token";
const USER_KEY = "promptshield_user";

// ===============================
// TOKEN
// ===============================

export function saveToken(token) {
    localStorage.setItem(TOKEN_KEY, token);
}

export function getToken() {
    return localStorage.getItem(TOKEN_KEY);
}

export function removeToken() {
    localStorage.removeItem(TOKEN_KEY);
}

// ===============================
// USER
// ===============================

export function saveUser(user) {
    localStorage.setItem(
        USER_KEY,
        JSON.stringify(user)
    );
}

export function getUser() {
    const user = localStorage.getItem(USER_KEY);

    return user ? JSON.parse(user) : null;
}

export function removeUser() {
    localStorage.removeItem(USER_KEY);
}

// ===============================
// AUTH
// ===============================

export function clearAuth() {
    removeToken();
    removeUser();
}

export function isAuthenticated() {
    return !!getToken();
}
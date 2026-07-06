import api from "./api";

export async function loginUser(credentials) {

    const response = await api.post(
        "/auth/login",
        {
            username: credentials.username,
            password: credentials.password,
        }
    );

    return response.data;

}
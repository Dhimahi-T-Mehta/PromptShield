import { Navigate } from "react-router-dom";

import { useAuth } from "../auth/useAuth";

export default function RoleProtectedRoute({

    children,

    allowedRoles,

}) {

    const {

        user,

        loading,

        isAuthenticated,

    } = useAuth();

    if (loading) {

        return null;

    }

    if (!isAuthenticated) {

        return <Navigate to="/login" replace />;

    }

    if (!allowedRoles.includes(user.role)) {

        return <Navigate to="/login" replace />;

    }

    return children;

}
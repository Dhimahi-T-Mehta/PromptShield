import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Navigate } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import Dashboard from "./pages/Dashboard";
import AnalystDashboard from "./pages/AnalystDashboard";

import ProtectedRoute from "./routes/ProtectedRoute";
import RoleProtectedRoute from "./routes/RoleProtectedRoute";

function App() {

    return (

        <BrowserRouter>

            <Routes>

                <Route
                    path="*"
                    element={<Navigate to="/login" replace />}
                />

                <Route
                    path="/analyst"
                    element={
                        <RoleProtectedRoute
                            allowedRoles={[
                                "analyst",
                                "admin",
                            ]}
                        >
                            <AnalystDashboard />
                        </RoleProtectedRoute>
                    }
                />

                <Route
                    path="/admin"
                    element={
                        <RoleProtectedRoute
                            allowedRoles={[
                                "admin",
                            ]}
                        >
                            <Dashboard />
                        </RoleProtectedRoute>
                    }
                />

                <Route
                    path="/login"
                    element={<LoginPage />}
                />

            </Routes>

        </BrowserRouter>

    );

}

export default App;
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import {
    FiUser,
    FiLock,
    FiEye,
    FiEyeOff,
} from "react-icons/fi";

import {
    FaSpinner,
} from "react-icons/fa";

import { motion } from "framer-motion";

import { useAuth } from "../../auth/useAuth";

export default function LoginForm() {

    const { login } = useAuth();

    const [username, setUsername] = useState("");

    const [password, setPassword] = useState("");

    const [remember, setRemember] = useState(true);

    const [showPassword, setShowPassword] = useState(false);

    const [loading, setLoading] = useState(false);

    const [error, setError] = useState("");

    const navigate = useNavigate();

async function handleSubmit(e) {

    e.preventDefault();

    setError("");

    setLoading(true);

    try {

        console.log("Submitting login...");

        const user = await login({

            username,

            password,

            remember,

        });

        console.log("Login successful:", user);

        if (user.role === "admin") {
            navigate("/admin", { replace: true });
        }
        else if (user.role === "analyst") {
            navigate("/analyst", { replace: true });
        }
        else {
            setError("This account has no assigned role.");
            return;
        }
    }

    catch (err) {

        console.error("LOGIN FAILED");

        console.error(err);

        console.error(err?.response);

        console.error(err?.response?.data);

        setError(

            err?.response?.data?.detail ||

            err.message ||

            "Unable to sign in."

        );

    }

    finally {

        setLoading(false);

    }

}

    return (

        <form
            className="login-form"
            onSubmit={handleSubmit}
        >

            {/* USERNAME */}

            <div className="input-group">

                <FiUser className="input-icon" />

                <input

                    type="text"

                    placeholder="Username"

                    value={username}

                    onChange={(e) =>
                        setUsername(e.target.value)
                    }

                    required

                />

            </div>

            {/* PASSWORD */}

            <div className="input-group">

                <FiLock className="input-icon" />

                <input

                    type={
                        showPassword
                            ? "text"
                            : "password"
                    }

                    placeholder="Password"

                    value={password}

                    onChange={(e) =>
                        setPassword(e.target.value)
                    }

                    required

                />

                <button

                    type="button"

                    className="password-toggle"

                    onClick={() =>
                        setShowPassword(!showPassword)
                    }

                >

                    {showPassword
                        ? <FiEyeOff />
                        : <FiEye />
                    }

                </button>

            </div>

            {/* OPTIONS */}

            <div className="login-options">

                <label className="remember-me">

                    <input

                        type="checkbox"

                        checked={remember}

                        onChange={(e) =>
                            setRemember(e.target.checked)
                        }

                    />

                    Remember Me

                </label>

                <button

                    type="button"

                    className="forgot-password"

                >

                    Forgot Password?

                </button>

            </div>

            {/* ERROR */}

            {error && (

                <motion.div

                    className="login-error"

                    initial={{
                        x: -10,
                        opacity: 0,
                    }}

                    animate={{
                        x: [0, -8, 8, -6, 0],
                        opacity: 1,
                    }}

                    transition={{
                        duration: 0.45,
                    }}

                >

                    {error}

                </motion.div>

            )}

            {/* BUTTON */}

            <motion.button

                whileHover={{
                    scale: 1.02,
                }}

                whileTap={{
                    scale: 0.98,
                }}

                disabled={loading}

                className="login-button"

                type="submit"

            >

                {

                    loading

                        ?

                        <>

                            <FaSpinner
                                className="spinner"
                            />

                            Signing In...

                        </>

                        :

                        "SIGN IN"

                }

            </motion.button>

        </form>

    );

}
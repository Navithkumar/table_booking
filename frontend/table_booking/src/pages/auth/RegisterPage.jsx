import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { registerApi } from '../../api/auth.api';

export default function RegisterPage() {
    const navigate = useNavigate();
    const [form, setForm] = useState({
        username: '',
        email: '',
        phone_number: '',
        password: '',
        role: 1,
    });

    const submit = async (e) => {
        e.preventDefault();
        const payload = {
            ...form,
            role: 1,
        };
        await registerApi(payload);
        navigate('/login');
    };

    return (
        <div className="container mt-5">
            <div className="row justify-content-center">
                <div className="col-md-4">
                    <div className="card shadow">
                        <div className="card-body">
                            <h4 className="text-center mb-3">Register</h4>

                            <form onSubmit={submit}>
                                {/* Username */}
                                <div className="mb-3">
                                    <label className="form-label">
                                        Username
                                    </label>
                                    <input
                                        className="form-control"
                                        required
                                        onChange={(e) =>
                                            setForm({
                                                ...form,
                                                username: e.target.value,
                                            })
                                        }
                                    />
                                </div>

                                {/* Email */}
                                <div className="mb-3">
                                    <label className="form-label">Email</label>
                                    <input
                                        className="form-control"
                                        type="email"
                                        required
                                        onChange={(e) =>
                                            setForm({
                                                ...form,
                                                email: e.target.value,
                                            })
                                        }
                                    />
                                </div>

                                {/* Phone */}
                                <div className="mb-3">
                                    <label className="form-label">Phone</label>
                                    <input
                                        className="form-control"
                                        type="tel"
                                        required
                                        onChange={(e) =>
                                            setForm({
                                                ...form,
                                                phone_number: e.target.value,
                                            })
                                        }
                                    />
                                </div>

                                {/* Password */}
                                <div className="mb-3">
                                    <label className="form-label">
                                        Password
                                    </label>
                                    <input
                                        className="form-control"
                                        type="password"
                                        required
                                        onChange={(e) =>
                                            setForm({
                                                ...form,
                                                password: e.target.value,
                                            })
                                        }
                                    />
                                </div>

                                <button className="btn btn-success w-100">
                                    Register
                                </button>
                            </form>

                            <div className="text-center mt-3">
                                <Link to="/login">
                                    Already have an account?
                                </Link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

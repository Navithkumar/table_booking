import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { loginApi } from '../../api/auth.api';
import useAuth from '../../hooks/useAuth';

export default function LoginPage() {
    const { loginUser } = useAuth();
    const navigate = useNavigate();
    const [form, setForm] = useState({ email: '', password: '' });
    const [error, setError] = useState('');

    const submit = async (e) => {
        e.preventDefault();
        try {
            const res = await loginApi(form);
            await loginUser(res.data.access);
            navigate('/dashboard');
        } catch {
            setError('Invalid email or password');
        }
    };

    return (
        <div className="container mt-5">
            <div className="row justify-content-center">
                <div className="col-md-4">
                    <div className="card shadow">
                        <div className="card-body">
                            <h4 className="text-center mb-3">
                                Restaurant Login
                            </h4>

                            {error && (
                                <div className="alert alert-danger">
                                    {error}
                                </div>
                            )}

                            <form onSubmit={submit}>
                                <div className="mb-3">
                                    <label>Email</label>
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

                                <div className="mb-3">
                                    <label>Password</label>
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

                                <button className="btn btn-primary w-100">
                                    Login
                                </button>
                            </form>

                            <div className="text-center mt-3">
                                <Link to="/register">Create an account</Link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

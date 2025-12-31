import { useEffect, useState } from 'react';
import { profileApi } from '../api/auth.api';
import AuthContext from './AuthContext';

export default function AuthProvider({ children }) {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    const loginUser = async (token) => {
        localStorage.setItem('accessToken', token);
        await fetchUser();
    };

    const logoutUser = () => {
        localStorage.removeItem('accessToken');
        setUser(null);
    };

    const fetchUser = async () => {
        try {
            const res = await profileApi();
            setUser(res.data);
        } catch {
            logoutUser();
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchUser();
    }, []);

    return (
        <AuthContext.Provider value={{ user, loginUser, logoutUser, loading }}>
            {children}
        </AuthContext.Provider>
    );
}

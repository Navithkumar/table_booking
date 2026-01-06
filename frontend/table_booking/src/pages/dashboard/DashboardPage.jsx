import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Dashboard.css';

export default function DashboardPage() {
    const [active, setActive] = useState('users');
    const [usersOpen, setUsersOpen] = useState(true);
    const [ordersOpen, setOrdersOpen] = useState(false);
    const [menuOpen, setMenuOpen] = useState(false);
    const [tablesOpen, setTablesOpen] = useState(false);

    const navigate = useNavigate();

    const logout = () => {
        localStorage.clear();
        navigate('/login');
    };

    const renderContent = () => {
        switch (active) {
            case 'users':
                return <h3>Users</h3>;
            case 'add-user':
                return <h3>Add User</h3>;
            case 'orders':
                return <h3>Orders</h3>;
            case 'add-order':
                return <h3>Create Order</h3>;
            case 'menu':
                return <h3>Menu</h3>;
            case 'add-menu':
                return <h3>Add Menu</h3>;
            case 'tables':
                return <h3>Tables</h3>;
            case 'add-table':
                return <h3>Add Table</h3>;
            default:
                return null;
        }
    };

    return (
        <div className="app-layout">
            {/* SIDEBAR */}
            <aside className="sidebar">
                {/* APP HEADER */}
                <div className="sidebar-header">
                    <div className="app-icon">🍽️</div>
                    <div>
                        <div className="app-name">Restaurant</div>
                    </div>
                </div>

                {/* USERS */}
                <div className="sidebar-section">
                    <div
                        className="sidebar-item parent"
                        onClick={() => setUsersOpen(!usersOpen)}
                    >
                        Users
                        <span className="arrow">{usersOpen ? '▾' : '▸'}</span>
                    </div>

                    {usersOpen && (
                        <div className="sidebar-children">
                            <div
                                className={`sidebar-item ${
                                    active === 'users' ? 'active' : ''
                                }`}
                                onClick={() => setActive('users')}
                            >
                                View Users
                            </div>
                            <div
                                className={`sidebar-item ${
                                    active === 'add-user' ? 'active' : ''
                                }`}
                                onClick={() => setActive('add-user')}
                            >
                                Add User
                            </div>
                        </div>
                    )}
                </div>

                <div className="sidebar-divider" />

                {/* ORDERS */}
                <div className="sidebar-section">
                    <div
                        className="sidebar-item parent"
                        onClick={() => setOrdersOpen(!ordersOpen)}
                    >
                        Orders
                        <span className="arrow">{ordersOpen ? '▾' : '▸'}</span>
                    </div>

                    {ordersOpen && (
                        <div className="sidebar-children">
                            <div
                                className={`sidebar-item ${
                                    active === 'orders' ? 'active' : ''
                                }`}
                                onClick={() => setActive('orders')}
                            >
                                View Orders
                            </div>
                            <div
                                className={`sidebar-item ${
                                    active === 'add-order' ? 'active' : ''
                                }`}
                                onClick={() => setActive('add-order')}
                            >
                                Create Order
                            </div>
                        </div>
                    )}
                </div>

                <div className="sidebar-divider" />

                {/* MENU */}
                <div className="sidebar-section">
                    <div
                        className="sidebar-item parent"
                        onClick={() => setMenuOpen(!menuOpen)}
                    >
                        Menu
                        <span className="arrow">{menuOpen ? '▾' : '▸'}</span>
                    </div>

                    {menuOpen && (
                        <div className="sidebar-children">
                            <div
                                className={`sidebar-item ${
                                    active === 'menu' ? 'active' : ''
                                }`}
                                onClick={() => setActive('menu')}
                            >
                                View Menu
                            </div>
                            <div
                                className={`sidebar-item ${
                                    active === 'add-menu' ? 'active' : ''
                                }`}
                                onClick={() => setActive('add-menu')}
                            >
                                Add Menu
                            </div>
                        </div>
                    )}
                </div>
                <div className="sidebar-divider" />
                {/* TABLES */}
                <div className="sidebar-section">
                    <div
                        className="sidebar-item parent"
                        onClick={() => setTablesOpen(!tablesOpen)}
                    >
                        Tables
                        <span className="arrow">{tablesOpen ? '▾' : '▸'}</span>
                    </div>

                    {tablesOpen && (
                        <div className="sidebar-children">
                            <div
                                className={`sidebar-item ${
                                    active === 'tables' ? 'active' : ''
                                }`}
                                onClick={() => setActive('tables')}
                            >
                                View Tables
                            </div>
                            <div
                                className={`sidebar-item ${
                                    active === 'add-table' ? 'active' : ''
                                }`}
                                onClick={() => setActive('add-table')}
                            >
                                Add Table
                            </div>
                        </div>
                    )}
                </div>
            </aside>

            {/* MAIN AREA */}
            <div className="main">
                <header className="topbar">
                    <span className="page-title">
                        {active.replace('-', ' ').toUpperCase()}
                    </span>
                    <button className="logout-btn" onClick={logout}>
                        Logout
                    </button>
                </header>

                <main className="content">{renderContent()}</main>
            </div>
        </div>
    );
}

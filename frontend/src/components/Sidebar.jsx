import {
    LayoutDashboard,
    Map,
    Satellite,
    AlertTriangle,
    ClipboardCheck,
    Settings,
    Shield
} from "lucide-react";

function Sidebar() {

    return (

        <aside className="sidebar">

            <div className="brand">

                <div className="brand-logo">
                    S34
                </div>

                <div>
                    <h2>RESPONSE</h2>
                    <span>DISASTER INTELLIGENCE</span>
                </div>

            </div>


            <div className="section-label">
                COMMAND CENTER
            </div>


            <nav>

                <div className="nav-item active">
                    <LayoutDashboard size={18} />
                    <span>Dashboard</span>
                </div>

                <div className="nav-item">
                    <Map size={18} />
                    <span>Live Map</span>
                </div>

                <div className="nav-item">
                    <Satellite size={18} />
                    <span>Imagery</span>
                </div>

                <div className="nav-item">
                    <AlertTriangle size={18} />
                    <span>Incidents</span>
                    <b>12</b>
                </div>

                <div className="nav-item">
                    <ClipboardCheck size={18} />
                    <span>Verification</span>
                    <b className="orange">7</b>
                </div>

            </nav>


            <div className="sidebar-bottom">

                <div className="nav-item">
                    <Settings size={18} />
                    <span>Settings</span>
                </div>


                <div className="system">

                    <span className="system-dot"></span>

                    <div>
                        <strong>Systems Operational</strong>
                        <small>
                            Last sync 2 min ago
                        </small>
                    </div>

                </div>

            </div>

        </aside>
    );
}

export default Sidebar;
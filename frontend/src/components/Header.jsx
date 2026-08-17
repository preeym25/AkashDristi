import {
    Search,
    Bell,
    Radio
} from "lucide-react";

function Header({
    disaster,
    search,
    setSearch
}) {

    return (

        <header className="header">

            <div>

                <div className="breadcrumb">
                    COMMAND CENTER / OVERVIEW
                </div>

                <h1>
                    {disaster.name}
                </h1>

                <p className="subtitle">
                    Post-disaster damage assessment
                    and relief prioritization
                </p>

            </div>


            <div className="header-actions">

                <div className="live-status">

                    <span></span>

                    <Radio size={14} />

                    LIVE

                </div>


                <div className="search-box">

                    <Search size={16} />

                    <input
                        value={search}
                        onChange={(e) =>
                            setSearch(e.target.value)
                        }
                        placeholder="Search incidents..."
                    />

                </div>


                <button className="notification">
                    <Bell size={18} />
                </button>


                <div className="profile">

                    <div className="avatar">
                        NR
                    </div>

                    <div>
                        <strong>Responder</strong>
                        <small>Emergency Ops</small>
                    </div>

                </div>

            </div>

        </header>
    );
}

export default Header;
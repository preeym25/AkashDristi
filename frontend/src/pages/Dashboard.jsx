import { useState } from "react";

import Sidebar from "../components/Sidebar";
import Header from "../components/Header";
import StatsCards from "../components/StatsCards";
import DisasterMap from "../components/DisasterMap";
import IncidentList from "../components/IncidentList";
import IncidentDetails from "../components/IncidentDetails";

import { disaster, incidents } from "../data/mockData";

function Dashboard() {

    const [selectedIncident, setSelectedIncident] =
        useState(null);

    const [filter, setFilter] =
        useState("ALL");

    const [search, setSearch] =
        useState("");

    const filteredIncidents = incidents.filter((incident) => {

        const matchesFilter =
            filter === "ALL" ||
            incident.priority === filter;

        const matchesSearch =
            incident.type
                .toLowerCase()
                .includes(search.toLowerCase());

        return matchesFilter && matchesSearch;
    });


    return (

        <div className="app">

            <Sidebar />

            <main className="main">

                <Header
                    disaster={disaster}
                    search={search}
                    setSearch={setSearch}
                />

                <StatsCards
                    incidents={incidents}
                    disaster={disaster}
                />


                <div className="dashboard-grid">

                    <section className="map-section">

                        <DisasterMap
                            incidents={filteredIncidents}
                            selectedIncident={selectedIncident}
                            setSelectedIncident={
                                setSelectedIncident
                            }
                            filter={filter}
                            setFilter={setFilter}
                        />

                    </section>


                    <section className="right-panel">

                        {selectedIncident ? (

                            <IncidentDetails
                                incident={selectedIncident}
                                close={() =>
                                    setSelectedIncident(null)
                                }
                            />

                        ) : (

                            <IncidentList
                                incidents={filteredIncidents}
                                selectIncident={
                                    setSelectedIncident
                                }
                            />

                        )}

                    </section>

                </div>

            </main>

        </div>
    );
}

export default Dashboard;
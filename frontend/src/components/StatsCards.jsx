import {
    AlertTriangle,
    Building2,
    Users,
    ClipboardCheck
} from "lucide-react";

function StatsCards({
    incidents,
    disaster
}) {

    const critical =
        incidents.filter(
            i => i.priority === "CRITICAL"
        ).length;

    const buildings =
        incidents.filter(
            i => i.type === "Building"
        ).length;

    return (

        <div className="stats-grid">

            <div className="stat-card">

                <div className="stat-icon red">
                    <AlertTriangle />
                </div>

                <div>
                    <span>Critical Incidents</span>
                    <strong>{critical}</strong>
                    <small>
                        Immediate action required
                    </small>
                </div>

            </div>


            <div className="stat-card">

                <div className="stat-icon orange">
                    <Building2 />
                </div>

                <div>
                    <span>Affected Structures</span>
                    <strong>{buildings}</strong>
                    <small>
                        Detected in current area
                    </small>
                </div>

            </div>


            <div className="stat-card">

                <div className="stat-icon blue">
                    <Users />
                </div>

                <div>
                    <span>People at Risk</span>
                    <strong>
                        {disaster.population.toLocaleString()}
                    </strong>
                    <small>
                        Estimated population
                    </small>
                </div>

            </div>


            <div className="stat-card">

                <div className="stat-icon purple">
                    <ClipboardCheck />
                </div>

                <div>
                    <span>Verification Queue</span>
                    <strong>07</strong>
                    <small>
                        Awaiting responder review
                    </small>
                </div>

            </div>

        </div>
    );
}

export default StatsCards;
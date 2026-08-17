import {
    AlertTriangle,
    Building2,
    MapPin
} from "lucide-react";

function IncidentList({
    incidents,
    selectIncident
}) {

    return (

        <div className="incident-list">

            <div className="panel-title">

                <div>

                    <span>DETECTED INCIDENTS</span>

                    <h2>
                        Priority Queue
                    </h2>

                </div>

                <span className="count">
                    {incidents.length}
                </span>

            </div>


            <div className="list">

                {incidents.map((incident) => (

                    <div
                        key={incident.id}
                        className="incident-row"
                        onClick={() =>
                            selectIncident(incident)
                        }
                    >

                        <div className={
                            `incident-symbol ${incident.priority.toLowerCase()}`
                        }>

                            {incident.type === "Building"
                                ? <Building2 size={18} />
                                : <AlertTriangle size={18} />
                            }

                        </div>


                        <div className="incident-info">

                            <div className="incident-name">

                                <strong>
                                    {incident.type}
                                </strong>

                                <span className={
                                    incident.priority.toLowerCase()
                                }>
                                    {incident.priority}
                                </span>

                            </div>


                            <div className="incident-meta">

                                <span>
                                    {incident.damage} damage
                                </span>

                                <span>
                                    {Math.round(
                                        incident.confidence * 100
                                    )}% confidence
                                </span>

                            </div>


                            <div className="incident-location">

                                <MapPin size={11} />

                                {incident.lat.toFixed(4)},
                                {" "}
                                {incident.lng.toFixed(4)}

                            </div>

                        </div>

                    </div>

                ))}

            </div>

        </div>
    );
}

export default IncidentList;
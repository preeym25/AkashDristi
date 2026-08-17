import {
    X,
    MapPin,
    ShieldCheck,
    Users,
    Route,
    Hospital,
    CheckCircle,
    XCircle,
    HelpCircle
} from "lucide-react";

function IncidentDetails({
    incident,
    close
}) {

    return (

        <div className="details-panel">

            <div className="details-header">

                <div>

                    <span>
                        INCIDENT #{incident.id}
                    </span>

                    <h2>
                        {incident.type}
                    </h2>

                </div>


                <button onClick={close}>
                    <X size={18} />
                </button>

            </div>


            <div className={
                `priority-banner ${incident.priority.toLowerCase()}`
            }>

                <div>

                    <span>RELIEF PRIORITY</span>

                    <strong>
                        {incident.priority}
                    </strong>

                </div>

                <div className="priority-score">
                    0.87
                </div>

            </div>


            <div className="damage-section">

                <span className="label">
                    DAMAGE ASSESSMENT
                </span>

                <div className="damage-value">

                    <strong>
                        {incident.damage}
                    </strong>

                    <span>
                        Damage severity
                    </span>

                </div>


                <div className="confidence-bar">

                    <div className="confidence-label">

                        <span>
                            AI Confidence
                        </span>

                        <strong>
                            {Math.round(
                                incident.confidence * 100
                            )}%
                        </strong>

                    </div>


                    <div className="bar">

                        <div
                            style={{
                                width:
                                    `${incident.confidence * 100}%`
                            }}
                        />

                    </div>

                </div>

            </div>


            <div className="evidence-box">

                <div className="evidence-title">

                    <ShieldCheck size={17} />

                    <strong>
                        Evidence & Provenance
                    </strong>

                </div>


                <div className="evidence-row">

                    <span>Source</span>

                    <strong>
                        Post-disaster imagery
                    </strong>

                </div>

                <div className="evidence-row">

                    <span>Analysis</span>

                    <strong>
                        Damage detection
                    </strong>

                </div>

                <div className="evidence-row">

                    <span>Confidence</span>

                    <strong>
                        {Math.round(
                            incident.confidence * 100
                        )}%
                    </strong>

                </div>

            </div>


            <div className="context-section">

                <span className="label">
                    RESPONSE CONTEXT
                </span>


                <div className="context-grid">

                    <div>

                        <Users />

                        <span>
                            Population
                        </span>

                        <strong>
                            {incident.population}
                        </strong>

                    </div>


                    <div>

                        <ShieldCheck />

                        <span>
                            Vulnerability
                        </span>

                        <strong>
                            {incident.vulnerability}
                        </strong>

                    </div>


                    <div>

                        <Route />

                        <span>
                            Road Status
                        </span>

                        <strong>
                            {incident.roadStatus}
                        </strong>

                    </div>


                    <div>

                        <Hospital />

                        <span>
                            Hospital
                        </span>

                        <strong>
                            {incident.hospitalDistance}
                        </strong>

                    </div>

                </div>

            </div>


            <div className="location">

                <MapPin size={16} />

                <div>

                    <span>LOCATION</span>

                    <strong>
                        {incident.lat},
                        {" "}
                        {incident.lng}
                    </strong>

                </div>

            </div>


            <div className="verification">

                <span className="label">
                    HUMAN VERIFICATION
                </span>

                <p>
                    AI-generated assessments require
                    responder confirmation before
                    operational action.
                </p>


                <div className="verification-buttons">

                    <button className="confirm">

                        <CheckCircle size={16} />

                        Confirm

                    </button>


                    <button className="reject">

                        <XCircle size={16} />

                        Reject

                    </button>


                    <button className="uncertain">

                        <HelpCircle size={16} />

                        Uncertain

                    </button>

                </div>

            </div>

        </div>
    );
}

export default IncidentDetails;
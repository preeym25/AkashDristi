import {
    useEffect,
    useRef
} from "react";

import {
    Map,
    NavigationControl,
    Marker
} from "maplibre-gl";

import "maplibre-gl/dist/maplibre-gl.css";


function DisasterMap({
    incidents,
    selectedIncident,
    setSelectedIncident,
    filter,
    setFilter
}) {

    const mapContainer = useRef(null);
    const map = useRef(null);
    const markers = useRef([]);


    // Initialize map
    useEffect(() => {

        if (map.current) return;

        map.current = new Map({

            container: mapContainer.current,

            style: {

                version: 8,

                sources: {

                    osm: {

                        type: "raster",

                        tiles: [
                            "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
                        ],

                        tileSize: 256,

                        attribution:
                            "© OpenStreetMap contributors"
                    }
                },

                layers: [

                    {
                        id: "osm",

                        type: "raster",

                        source: "osm"
                    }

                ]
            },

            center: [
                77.2090,
                28.6139
            ],

            zoom: 12
        });


        map.current.addControl(
            new NavigationControl(),
            "top-right"
        );


        return () => {

            if (map.current) {

                map.current.remove();

                map.current = null;

            }

        };

    }, []);


    // Add incident markers
    useEffect(() => {

        if (!map.current) return;


        // Remove old markers
        markers.current.forEach(
            marker => marker.remove()
        );

        markers.current = [];


        // Add new markers
        incidents.forEach((incident) => {

            const element =
                document.createElement("div");

            element.className =
                "incident-marker";


            if (incident.priority === "CRITICAL") {

                element.classList.add("critical");

            } else if (incident.priority === "HIGH") {

                element.classList.add("high");

            } else if (incident.priority === "MEDIUM") {

                element.classList.add("medium");

            } else {

                element.classList.add("low");

            }


            element.addEventListener(
                "click",
                () => {

                    setSelectedIncident(incident);

                }
            );


            const marker =
                new Marker({
                    element
                })
                    .setLngLat([
                        incident.lng,
                        incident.lat
                    ])
                    .addTo(map.current);


            markers.current.push(marker);

        });


    }, [incidents, setSelectedIncident]);


    return (

        <div className="map-wrapper">

            {/* MAP HEADER */}

            <div className="map-topbar">

                <div className="map-heading">

                    <span className="pulse"></span>

                    <div>

                        <strong>
                            LIVE INCIDENT MAP
                        </strong>

                        <small>
                            {incidents.length}
                            {" "}active detections
                        </small>

                    </div>

                </div>


                {/* FILTER BUTTONS */}

                <div className="layer-controls">

                    {[
                        "ALL",
                        "CRITICAL",
                        "HIGH",
                        "MEDIUM",
                        "LOW"
                    ].map((item) => (

                        <button
                            key={item}

                            className={
                                filter === item
                                    ? "selected"
                                    : ""
                            }

                            onClick={() =>
                                setFilter(item)
                            }
                        >

                            {item}

                        </button>

                    ))}

                </div>

            </div>


            {/* MAP */}

            <div
                ref={mapContainer}
                className="map"
            />


            {/* LEGEND */}

            <div className="map-legend">

                <span>

                    <i className="critical-dot"></i>

                    Critical

                </span>


                <span>

                    <i className="high-dot"></i>

                    High

                </span>


                <span>

                    <i className="medium-dot"></i>

                    Medium

                </span>


                <span>

                    <i className="low-dot"></i>

                    Low

                </span>

            </div>


            {/* MAP INFORMATION */}

            <div className="map-info">

                <strong>
                    AOI
                </strong>

                <span>
                    42.8 km² affected area
                </span>

            </div>

        </div>

    );

}


export default DisasterMap;
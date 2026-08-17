export const disaster = {
    id: 1,
    name: "Delhi Flood 2026",
    type: "Flood",
    severity: "HIGH",
    affectedArea: "42.8 km²",
    population: 6000
};

export const incidents = [
    {
        id: 1,
        type: "Building",
        damage: "Severe",
        confidence: 0.94,
        priority: "CRITICAL",
        lat: 28.6145,
        lng: 77.2102,
        population: 126,
        vulnerability: "HIGH",
        roadStatus: "BLOCKED",
        hospitalDistance: "2.4 km",
        status: "pending"
    },

    {
        id: 2,
        type: "Building",
        damage: "Severe",
        confidence: 0.89,
        priority: "CRITICAL",
        lat: 28.6170,
        lng: 77.2150,
        population: 84,
        vulnerability: "HIGH",
        roadStatus: "BLOCKED",
        hospitalDistance: "3.1 km",
        status: "pending"
    },

    {
        id: 3,
        type: "Road",
        damage: "Severe",
        confidence: 0.87,
        priority: "HIGH",
        lat: 28.6110,
        lng: 77.2050,
        population: 320,
        vulnerability: "MEDIUM",
        roadStatus: "BLOCKED",
        hospitalDistance: "1.8 km",
        status: "pending"
    },

    {
        id: 4,
        type: "Building",
        damage: "Moderate",
        confidence: 0.81,
        priority: "HIGH",
        lat: 28.6200,
        lng: 77.2080,
        population: 61,
        vulnerability: "MEDIUM",
        roadStatus: "OPEN",
        hospitalDistance: "1.2 km",
        status: "pending"
    },

    {
        id: 5,
        type: "Road",
        damage: "Moderate",
        confidence: 0.76,
        priority: "MEDIUM",
        lat: 28.6070,
        lng: 77.2180,
        population: 180,
        vulnerability: "MEDIUM",
        roadStatus: "PARTIALLY BLOCKED",
        hospitalDistance: "2.8 km",
        status: "pending"
    },

    {
        id: 6,
        type: "Building",
        damage: "Minor",
        confidence: 0.72,
        priority: "LOW",
        lat: 28.6250,
        lng: 77.2020,
        population: 32,
        vulnerability: "LOW",
        roadStatus: "OPEN",
        hospitalDistance: "900 m",
        status: "pending"
    }
];
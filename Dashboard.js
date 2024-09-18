// Dashboard.js (React component)

import React, { useState, useEffect } from 'react';

function Dashboard() {
    const [data, setData] = useState([]);
    
    useEffect(() => {
        fetch('/optimize', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ locations: [/* Sample data */] })
        })
        .then(response => response.json())
        .then(data => setData(data));
    }, []);

    return (
        <div>
            <h2>Optimized Waste Collection Routes</h2>
            <ul>
                {data.map((location, index) => (
                    <li key={index}>Location {location}</li>
                ))}
            </ul>
        </div>
    );
}

export default Dashboard;

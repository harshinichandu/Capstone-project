-- PostgreSQL schema
CREATE TABLE waste_data (
    id SERIAL PRIMARY KEY,
    location VARCHAR(255),
    waste_volume INT,
    collection_date DATE
);

-- SQL script to create the table unique_id on the MySQL server

-- Query to create the table if it does not already exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

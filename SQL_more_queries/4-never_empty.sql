-- SQL script to create the table id_not_null on the MySQL server

-- Query to create the table if it does not already exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

-- SQL script to create the database hbtn_0d_usa and the table states on the MySQL server

-- Query to create the database if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Query to use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Query to create the table if it does not already exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

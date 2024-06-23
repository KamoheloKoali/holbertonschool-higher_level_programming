-- SQL script to create the database hbtn_0d_2 and the user user_0d_2

-- Query to create the database if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Query to create user user_0d_2 if it does not already exist and set password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Query to grant SELECT privilege to user_0d_2 on database hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

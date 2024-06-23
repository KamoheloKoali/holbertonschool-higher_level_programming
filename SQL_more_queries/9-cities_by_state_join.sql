-- SQL query to list all cities with their corresponding state names in the database hbtn_0d_usa using JOIN

-- Query to list all cities with their corresponding state names and sort by cities.id
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;

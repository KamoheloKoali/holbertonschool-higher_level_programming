-- SQL query to list all cities of California in the database hbtn_0d_usa using subquery

-- Query to retrieve the state_id for California from the states table
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id
AND states.name = 'California'
ORDER BY cities.id ASC;

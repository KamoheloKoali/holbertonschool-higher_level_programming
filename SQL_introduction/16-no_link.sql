-- Script that list all records with a non-null name value, ordered by descending score
-- SQL command to list records with score and name, filtering out rows without a name value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

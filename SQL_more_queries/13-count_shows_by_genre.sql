-- SQL query to list all genres from hbtn_0d_tvshows and display the number of shows linked to each

-- Query to list all genres with the number of shows linked to each, excluding genres with no linked shows, and sort by number of shows linked
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
ORDER BY number_of_shows DESC;

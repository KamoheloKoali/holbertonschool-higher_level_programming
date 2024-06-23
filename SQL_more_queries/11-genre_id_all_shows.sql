-- SQL query to list all shows contained in the database hbtn_0d_tvshows, including NULL for shows without a genre

-- Query to list all shows with their corresponding genre_id (or NULL if no genre linked) and sort by title and genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

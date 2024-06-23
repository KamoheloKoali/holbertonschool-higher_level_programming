-- SQL query to list all shows with at least one genre linked in the hbtn_0d_tvshows database

-- Query to list all shows with at least one genre linked and sort by title and genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
    FROM tv_shows INNER JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id
    ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;

-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- First column: genre, Second column: number_of_shows
-- Only shows genres with at least one show, sorted by number_of_shows DESC
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;

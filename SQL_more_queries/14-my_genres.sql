-- Lists all genres of the show Dexter from the database hbtn_0d_tvshows
-- Uses a triple join to connect shows to genres via the junction table
SELECT name
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY name ASC;

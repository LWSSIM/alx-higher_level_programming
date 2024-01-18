-- Import the database dump from hbtn_0d_tvshows (same as 100-not_my_genres.sql)
--
-- Write a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
--
--   The tv_genres table contains only one record where name = Comedy (but the id can be different)
--   Each record should display: tv_shows.title
--   Results must be sorted in ascending order by the show title
--   You can use a maximum of two SELECT statement
--   The database name will be passed as an argument of the mysql command
SELECT tv_shows.title
FROM tv_shows
WHERE id NOT IN (
    SELECT ts.id
      FROM tv_shows ts
      JOIN tv_show_genres tsg ON ts.id = tsg.show_id
      JOIN tv_genres tg ON tsg.genre_id = tg.id
      WHERE tg.name = 'Comedy'
)
  ORDER BY title ASC;


-- Import the database dump from hbtn_0d_tvshows_rate (same as 102-rating_shows.sql)
--
-- Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
--
--   Each record should display: tv_genres.name - rating sum
--   Results must be sorted in descending order by their rating
--   You can use only one SELECT statement
--   The database name will be passed as an argument of the mysql command
SELECT g.name AS genre_name, SUM(r.rate) AS rating_sum
  FROM tv_genres g
  JOIN tv_show_genres sg ON g.id = sg.genre_id
  JOIN tv_show_ratings r ON r.show_id = sg.show_id
  GROUP BY g.name
  ORDER BY rating_sum DESC;



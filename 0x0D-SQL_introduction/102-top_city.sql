-- script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
-- Imported table dump in hbtn_0c_0 database from temperature.sql
SELECT city, AVG(value) AS avg_tmp
  FROM temperatures
  WHERE month = 7 OR month = 8
  GROUP BY city
  ORDER BY avg_tmp DESC
  LIMIT 3;

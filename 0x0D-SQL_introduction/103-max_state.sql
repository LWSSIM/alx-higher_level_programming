-- script that displays the max temperature of each state (ordered by State name).
-- Imported table dump in hbtn_0c_0 database from temperature.sql
SELECT state, MAX(value) AS max_temp
  FROM temperatures
  GROUP BY state
  ORDER BY state;


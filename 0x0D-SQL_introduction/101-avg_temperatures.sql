-- Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- Imported a table dump in hbtn_0c_0 database from temperature.sql
-- 'mysql -u your_username -p your_database < your_dump_file.sql'
SELECT city, AVG(value) AS avg_temp 
FROM temperatures 
GROUP BY city 
ORDER BY avg_temp DESC;


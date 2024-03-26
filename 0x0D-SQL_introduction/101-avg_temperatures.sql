-- This script showcases the average temperature (in Fahrenheit) for each city, arranged in descending order based on temperature.
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
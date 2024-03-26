-- This script presents the highest temperatures for cities during July and August, listed in descending order.
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month BETWEEN 7 and 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
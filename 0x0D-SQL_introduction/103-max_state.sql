-- This script showcases the maximum temperature for each state, arranged alphabetically by state name.
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
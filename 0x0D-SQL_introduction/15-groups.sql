This script enumerates the count of records sharing identical scores in the second_table.
SELECT score, COUNT(score) as number
FROM second_table
GROUP BY score
ORDER BY number DESC;
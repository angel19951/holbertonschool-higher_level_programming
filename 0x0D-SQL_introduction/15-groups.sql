-- Lists number of recors with the same score in a table
-- Ordered by descending count
SELECT score, COUNT('score') AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;

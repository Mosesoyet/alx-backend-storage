-- SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
-- Get Sum of fans per country first

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

-- SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
SELECT COUNT(id) AS total_band_members, origin
FROM metal_bands
GROUP BY origin
ORDER BY COUNT(id) DESC;

-- script to filter bands by type
-- SELECT band_name then use COALESCE() to find the year

SELECT band_name, COALESCE(split, 2020) - formed AS lifespan FROM
metal_bands WHERE
style LIKE "%Glam rock%" ORDER BY lifespan DESC;

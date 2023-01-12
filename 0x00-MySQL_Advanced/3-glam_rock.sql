-- script to filter bands by type

SELECT band_name, COALESCE(split, 2023) - formed as lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC;
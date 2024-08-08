-- SQL script to list all bands with Glam rock as their main style
-- The columns in the output are:
-- - band_name: The name of the band
-- - lifespan: The lifespan of the band in years until 2022
SELECT 
    name AS band_name,
    IFNULL(split, 2022) - formed AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;

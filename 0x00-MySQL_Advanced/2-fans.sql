-- SQL script to rank country origins of bands by the number of non-unique fans
-- - origin: The country of origin of the band
-- - nb_fans: The total number of (non-unique) fans from that country

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

-- Compute book loan duration

SELECT *
    , EXTRACT (DAY FROM AGE(dateretoureffective , dateemprunt)) AS DureeEmprunt
FROM Emprunts
WHERE dateretoureffective IS NOT NULL;
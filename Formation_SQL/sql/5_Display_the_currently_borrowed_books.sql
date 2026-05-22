-- Filter the current borrowed books
SELECT 
    L.titre
    , E.DateEmprunt
    , E.dateretoureffective
    , E.dateretourprevue
FROM Emprunts AS E
LEFT JOIN Livres AS L
    ON L.LivreID = E.LivreID
WHERE dateretoureffective IS NULL;
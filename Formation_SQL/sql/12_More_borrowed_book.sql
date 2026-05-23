-- More borrowed book

SELECT
    L.Titre
    , COUNT(L.Titre) AS NbLoans
FROM Emprunts AS E
LEFT JOIN Livres AS L
    ON L.LivreID = E.LivreID
GROUP BY L.Titre
ORDER BY COUNT(L.Titre) DESC
LIMIT 3;

-- OR 

SELECT
    L.Titre
    , COUNT(E.EmpruntID) AS NbLoans
FROM Emprunts AS E
INNER JOIN Livres AS L
    ON L.LivreID = E.LivreID
GROUP BY L.LivreID
ORDER BY NbLoans DESC
LIMIT 3;



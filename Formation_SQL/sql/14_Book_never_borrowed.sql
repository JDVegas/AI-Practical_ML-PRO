-- List of books never borrowed

SELECT
    L.Titre
FROM Livres  AS L
LEFT JOIN Emprunts AS E
    ON E.LivreID = L.LivreID
WHERE E.LivreID IS NULL;
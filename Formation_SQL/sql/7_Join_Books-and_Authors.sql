-- Join books and authors

SELECT 
    L.Titre
    , A.Nom
    , A.Prenom
FROM Livres AS L
LEFT JOIN Auteurs AS A
    ON A.AuteurID = L.AuteurID ;
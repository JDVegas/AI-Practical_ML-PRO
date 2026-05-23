-- Multiple Join
SELECT
    ET.Nom
    , ET.Prenom
    , L.Titre
    , G.NomGenre
FROM Emprunts AS E
FULL OUTER JOIN Livres AS L
    ON L.LivreID = E.LivreID
FULL OUTER JOIN Emprunteurs AS ET
    ON ET.EmprunteurID = E.EmprunteurID
FULL OUTER JOIN Genres AS G
    ON L.GenreID = G.GenreID
;



-- More strict display for only the complet rows
SELECT
    ET.Nom
    , ET.Prenom
    , L.Titre
    , G.NomGenre
FROM Emprunts AS E
LEFT JOIN Livres AS L
    ON L.LivreID = E.LivreID
LEFT JOIN Emprunteurs AS ET
    ON ET.EmprunteurID = E.EmprunteurID
LEFT JOIN Genres AS G
    ON L.GenreID = G.GenreID
;
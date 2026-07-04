-- Number of books by type

SELECT 
    G.NomGenre
    , Count(L.Titre) AS NumberOfBooks
FROM Livres AS L
LEFT JOIN Genres AS G
    ON G.genreID = L.genreID
GROUP BY G.NomGenre;

-- OR - Another way to do it 
SELECT
    G.NomGenre
    , COUNT(L.LivreID) AS NumberBooks
FROM Genres AS G
LEFT JOIN Livres AS L
    ON L.GenreID = G.GenreID
GROUP BY G.NomGenre;

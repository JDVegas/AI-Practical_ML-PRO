-- Number of books borrowed by loaner

SELECT
    ET.Nom
    , ET.Prenom
    , Count(E.LivreID) AS NumBorrowedBooks
FROM Emprunteurs AS ET
LEFT JOIN Emprunts As E
    ON E.EmprunteurID = ET.EmprunteurID
GROUP BY ET.Nom, ET.Prenom;
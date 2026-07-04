-- Loan duration mean by loaner

SELECT 
    ET.Nom
    , ET.Prenom
    , AVG(EXTRACT(DAY FROM AGE(dateretoureffective, dateemprunt))) AS MeanLoanDuration
    --, EXTRACT(DAY FROM AGE(dateretoureffective, dateemprunt)) AS TimeLoan
FROM Emprunteurs AS ET
INNER JOIN Emprunts AS E
    ON E.EmprunteurID = ET.EmprunteurID
WHERE DateRetourEffective IS NOT NULL
GROUP BY ET.Nom, ET.Prenom
;

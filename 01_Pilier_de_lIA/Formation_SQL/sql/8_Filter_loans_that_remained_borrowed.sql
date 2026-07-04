-- Filter loans that remained borrowed

SELECT 
    ET.Nom
    , ET.Prenom
    , ET.Email
FROM Emprunts AS E
LEFT JOIN Emprunteurs AS ET
    ON ET.emprunteurid = E.emprunteurid
WHERE dateretoureffective IS NULL
;
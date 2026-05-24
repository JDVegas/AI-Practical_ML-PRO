-- Number of loaner by Author

SELECT
    A.Nom
    , A.Prenom
    , COUNT(DISTINCT EmpruntID) AS NumEmprunts
FROM Auteurs AS A
LEFT JOIN Livres AS L
    ON L.AuteurID = A.AuteurID
LEFT JOIN Emprunts AS E
    ON E.livreID = L.LivreID
GROUP bY A.AuteurID, A.Nom, A.Prenom;



-- RUN THE SCRIPT 
-- From the terminal : psql -U postgres -d sandbox_db -f sql/15_Nb_Loaner_by_author.sql
-- It will be necessary to tip the password
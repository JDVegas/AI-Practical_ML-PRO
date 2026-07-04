-- Generate Database Schemas to create tables --


-- REMOVE TABLES IF ALREADY EXIST
DROP TABLE IF EXISTS livres CASCADE;
DROP TABLE IF EXISTS auteurs CASCADE;
DROP TABLE IF EXISTS genres CASCADE;
DROP TABLE IF EXISTS Emprunteurs CASCADE;
DROP TABLE IF EXISTS Emprunts CASCADE;



-- AUTEURS
CREATE TABLE Auteurs (
    AuteurID INT PRIMARY KEY
    , Nom TEXT
    , Prenom TEXT
    , Pays TEXT
);

-- GENRES
CREATE TABLE Genres(
    GenreID INT PRIMARY KEY
    , NomGenre TEXT
);


-- LIVRES
CREATE TABLE Livres (
    LivreID INT PRIMARY KEY
    , Titre TEXT
    , AuteurID INT
    , GenreID INT
    , DatePublication DATE
    , Disponible BOOLEAN
    , FOREIGN KEY (AuteurID) REFERENCES Auteurs (AuteurID)
    , FOREIGN KEY (GenreID)  REFERENCES Genres (GenreID)
);

-- EMPRUNTEURS
CREATE TABLE Emprunteurs (
    EmprunteurID INT PRIMARY KEY
    , Nom TEXT 
    , Prenom TEXT
    , Email TEXT
    , Telephone TEXT
);

-- EMPRUNTS
CREATE TABLE Emprunts (
    EmpruntID INT PRIMARY KEY
    , LivreID INT
    , EmprunteurID INT
    , DateEmprunt DATE
    , DateRetourPrevue DATE
    , DateRetourEffective DATE
    , FOREIGN KEY (LivreID) REFERENCES Livres (LivreID)
    , FOREIGN KEY (EmprunteurID) REFERENCES Emprunteurs (EmprunteurID)
);


-- PROTOCOL
-- 1. Within the Shell, tip the command `psql -U postgres -d sandbox_db -f sql/1_create_schemas.sql`
-- 2. Within the Shell, connect to the database `psql -U postgres -d sandbox_db`
-- 3. Within the Shell in the postgres server `sandbox_db=# \dt`



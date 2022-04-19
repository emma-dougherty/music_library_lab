DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR (100)
);

CREATE TABLE album (
    id SERIAL PRIMARY KEY,
    title VARCHAR (100),
    genre VARCHAR (100),
    artist_id INT REFERENCES artists(id)
);
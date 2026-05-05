CREATE DATABASE IF NOT EXISTS recommendation;
USE recommendation;

-- Create ratings Table
DROP TABLE IF EXISTS ratings;
CREATE TABLE ratings
(
	user_id			INT NOT NULL,
	movie_id 		INT NOT NULL,
	rating		TINYINT NOT NULL,
	timestamp		INT NOT NULL
);

LOAD DATA INFILE '/var/lib/mysql-files/u.data'
INTO TABLE ratings
FIELDS TERMINATED BY '\t'
ENCLOSED BY '"'
LINES TERMINATED BY '\n';


-- create table movies
DROP TABLE IF EXISTS movies;
CREATE TABLE movies
(

	movie_id			INT NOT NULL,
	movie_title		VARCHAR(255) NOT NULL,
	release_date		VARCHAR(255) NOT NULL,
	video_release_date		VARCHAR(10),
    imdb_url				VARCHAR(255) NOT NULL,
    unknown				TINYINT NOT NULL,
    action				TINYINT NOT NULL,
    adventure				TINYINT NOT NULL,
    animation				TINYINT NOT NULL,
    children				TINYINT NOT NULL,
    comedy				TINYINT NOT NULL,
    crime				TINYINT NOT NULL,
    documentary				TINYINT NOT NULL,
    drama				TINYINT NOT NULL,
    fantasay				TINYINT NOT NULL,
    film_Noir				TINYINT NOT NULL,
    horror				TINYINT NOT NULL,
    musical				TINYINT NOT NULL,
    mystery				TINYINT NOT NULL,
    romance				TINYINT NOT NULL,
    sci_fi				TINYINT NOT NULL,
    thriller				TINYINT NOT NULL,
    war				TINYINT NOT NULL,
    western				TINYINT NOT NULL
);

LOAD DATA INFILE '/var/lib/mysql-files/u.item'
INTO TABLE movies
CHARACTER SET latin1
FIELDS TERMINATED BY '|'
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
ALTER TABLE movies
DROP COLUMN video_release_date;

-- Create ratings Table
DROP TABLE IF EXISTS users;
CREATE TABLE users
(
	user_id			INT NOT NULL,
	age 		INT NOT NULL,
	gender		VARCHAR(10) NOT NULL,
	occupation		VARCHAR(255) NOT NULL,
    zip				VARCHAR(10) NOT NULL
);

LOAD DATA INFILE '/var/lib/mysql-files/u.user'
INTO TABLE users
FIELDS TERMINATED BY '|'
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
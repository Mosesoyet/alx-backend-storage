-- Create table if dose not exists users on the holberton database

CREATE TABLE users(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);

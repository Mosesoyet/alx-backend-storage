-- Create table if dose not exists users on the holberton database

CREATE TABLE users(
	id INTEGER PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);

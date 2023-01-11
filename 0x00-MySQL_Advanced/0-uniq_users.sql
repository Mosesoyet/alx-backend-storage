-- Create table if dose not exists users on the holberton database

-- Create database
CREATE DATABASE IF NOT EXISTS holberton;

USE holberton;

CREATE TABLE users(
	id INTEGER PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);

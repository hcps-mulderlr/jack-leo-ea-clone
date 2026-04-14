-- Run these commands in your database, replacing username with your username
-- Use postgres locally

CREATE DATABASE clone_lab;

\c clone_lab -- to connect to that database

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

INSERT INTO users (username, password) VALUES ('Mr. Miller', 'worldscoolestteacher');

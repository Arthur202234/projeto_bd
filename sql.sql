CREATE DATABASE IF NOT EXISTS gta6_db;
USE gta6_db;

CREATE TABLE IF NOT EXISTS jogadores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    nick_jogo VARCHAR(100) NOT NULL,
    vai_jogar VARCHAR(20) NOT NULL
);

select * from jogadores;
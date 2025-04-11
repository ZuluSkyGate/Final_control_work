-- Создание базы данных
CREATE DATABASE IF NOT EXISTS human_friends;
USE human_friends;

-- Создание таблицы для всех животных
CREATE TABLE animals (
    id INT PRIMARY KEY AUTO_INCREMENT,
    type VARCHAR(20),
    species VARCHAR(20),
    name VARCHAR(50),
    birth_date DATE,
    commands TEXT
);

-- Создание таблицы для молодых животных
CREATE TABLE young_animals (
    id INT PRIMARY KEY AUTO_INCREMENT,
    animal_id INT,
    age_months INT,
    FOREIGN KEY (animal_id) REFERENCES animals(id)
);

-- Вставка данных
INSERT INTO animals (type, species, name, birth_date, commands)
VALUES
    ('domestic', 'dog', 'Бобик', '2022-01-01', 'сидеть,лежать'),
    ('domestic', 'cat', 'Мурка', '2021-05-15', 'принести'),
    ('domestic', 'hamster', 'Хома', '2023-02-20', 'бежать в колесе'),
    ('pack', 'horse', 'Буцефал', '2020-07-10', 'галоп,рысь'),
    ('pack', 'donkey', 'Иа', '2021-12-01', 'стоять');

-- Создание представления для молодых животных
CREATE VIEW v_young_animals AS
SELECT
    a.*,
    TIMESTAMPDIFF(MONTH, a.birth_date, CURDATE()) as age_months
FROM
    animals a
WHERE
    TIMESTAMPDIFF(YEAR, a.birth_date, CURDATE()) BETWEEN 1 AND 3;
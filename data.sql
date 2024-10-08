CREATE DATABASE school_db;
USE school_db;

CREATE TABLE student (
    sno INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    sex ENUM('Male', 'Female'),
    class VARCHAR(50),
    fees DECIMAL(10, 2),
    `rank` INT,
    english_mark INT,
    python_mark INT,
    math_mark INT,
    class_teacher VARCHAR(100)
);

CREATE TABLE teacher (
    sno INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    sex ENUM('Male', 'Female'),
    salary DECIMAL(10, 2),
    class_teacher_class VARCHAR(50)
);

CREATE TABLE principal (
    sno INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    sex ENUM('Male', 'Female'),
    salary DECIMAL(10, 2)
);

CREATE TABLE admin (
    sno INT PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(100),
    password VARCHAR(100)
);

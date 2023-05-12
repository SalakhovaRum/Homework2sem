CREATE DATABASE online_school;

USE online_school;

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    last_name VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    group_id INT,
    FOREIGN KEY (group_id) REFERENCES groups(id)
);

CREATE TABLE teachers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    last_name VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    course_id INT,
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

CREATE TABLE courses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);

CREATE TABLE groups (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    course_id INT,
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

CREATE TABLE lessons (
    id INT PRIMARY KEY AUTO_INCREMENT,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    group_id INT,
    course_id INT,
    FOREIGN KEY (group_id) REFERENCES groups(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
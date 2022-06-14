CREATE DATABASE IF NOT EXISTS vmoa_proyectoscm;
USE vmoa_proyectoscm;

CREATE TABLE doctor(
    id INT(20) not null auto_increment,
    nombre VARCHAR(30) not null,
    apellidos VARCHAR(50) not null,
    cedula VARCHAR(20) not null,
    telefono VARCHAR(12) not null,
    consultorio VARCHAR (10) not null,
    especialidad VARCHAR(100) not null,
    email VARCHAR (255) not null,
    password VARCHAR(255) not null,
    CONSTRAINT pk_doctores PRIMARY KEY(id),
    CONSTRAINT uq_telefono UNIQUE(telefono),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE consultas(
    id INT (20) not null auto_increment,
    doctor_id INT (20) not null,
    nombre_paciente VARCHAR (100) not null,
    telefono VARCHAR(12) not null,
    edad SMALLINT not null,
    fecha DATE not null,
    CONSTRAINT pk_consultas PRIMARY KEY(id),
    CONSTRAINT fk_consulta_doctor FOREIGN KEY(doctor_id) REFERENCES doctor(id)
)ENGINE=InnoDb;
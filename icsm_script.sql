CREATE DATABASE IF NOT EXISTS icsm_final;
USE icsm_final;
CREATE TABLE doctores(
    id int(25) auto_increment not null,
    nombre varchar(100),
    apellidos varchar(255),
    cedula varchar(255),
    email  varchar(255),
    password varchar(255) not null,
    fecha date not null,
    CONSTRAINT pk_doctor PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE (email) 
)ENGINE = InnoDb;

CREATE TABLE consultorios(
    id int(25) auto_increment not null,
    consultorio varchar(70) not null,    
    CONSTRAINT pk_cconsultorios PRIMARY KEY(id)
)ENGINE=InnoDb;

CREATE TABLE citas(
    id int(25) auto_increment not null,
    doctor_id int(25) not null,
    consultorio_id int(25) not null,
    paciente varchar(100) not null,
    hora time not null,    
    fecha_cita date not null,
    fecha_creacion date not null,
    notas  MEDIUMTEXT,
    CONSTRAINT pk_citas PRIMARY KEY(id),
    CONSTRAINT fk_cita_doctor FOREIGN KEY(doctor_id) REFERENCES doctores(id),
    CONSTRAINT fk_cita_consultorio FOREIGN KEY(consultorio_id) REFERENCES consultorios(id)
)ENGINE=InnoDb;

INSERT INTO consultorios VALUES (NULL, "Consultorio1"),(NULL,"Consultorio2"),(NULL,"Consultorio3");

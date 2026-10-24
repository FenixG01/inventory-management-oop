-- 1. Creamos la base de datos
CREATE DATABASE IF NOT EXISTS inventary;
USE inventary;

-- 2. Borramos las tablas si ya existían (para evitar errores)
DROP TABLE IF EXISTS EMPLOYEE;
DROP TABLE IF EXISTS producto;

-- 3. Creamos la tabla de Empleados
CREATE TABLE EMPLOYEE (
  empId INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(100) NOT NULL,
  ape VARCHAR(100) NOT NULL,
  rfc VARCHAR(20) NOT NULL,
  acces VARCHAR(50) NOT NULL,
  rol VARCHAR(20) NOT NULL DEFAULT 'Empleado'
);

-- 4. Creamos la tabla de Productos
CREATE TABLE producto (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nam VARCHAR(150) NOT NULL,
  num INT NOT NULL,
  descr TEXT NOT NULL,  
  cant INT NOT NULL,
  est VARCHAR(50) NOT NULL
);

-- 5. Insertamos los usuarios de prueba (Administradores)
-- NOTA: El RFC funciona como contraseña.
INSERT INTO EMPLOYEE (nom, ape, rfc, acces, rol) VALUES 
('Samantha Mabeth', 'Esquer Lara', 'EULS060129HSUSRMA2', 'Samantha', 'Administrador'), 
('Claudio Tadeo', 'Lara Aviles', 'KLLO230JNMAMN178L1', 'Claudio', 'Administrador'),
('Sergio Gael', 'Villanueva Martínez', 'PELG060714HDGMRN08', 'Sergio', 'Administrador'), 
('Brandon', 'Martinez Gamboa', 'MAGB070909HDGRMRA7', 'Brandon', 'Administrador'); 

-- 6. Insertamos los usuarios de prueba (Empleados normales)
INSERT INTO EMPLOYEE (nom, ape, rfc, acces, rol) VALUES 
('Luis Alberto', 'Gómez Pérez', 'GOPL950412HDF', 'Luis', 'Empleado'), 
('Ana María', 'Sánchez Ruiz', 'SARA981123MDF', 'Ana', 'Empleado'),
('Carlos Javier', 'Díaz Torres', 'DITC010203HDF', 'Carlos', 'Empleado');
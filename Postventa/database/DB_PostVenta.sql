-------------------------------
create table Privilegio(
ID serial PRIMARY KEY, --autoincremental
Descripcion varchar(60) not null
);

select * from Privilegio;

insert into Privilegio (Descripcion) values
('Agregar Usuario'),
('Actualizar Usuario'),
('Eliminar Usuario'),
('Registrar Personal'),
('Modificar Personal'),
('Eliminar Personal'),
('Registrar Reserva'),
('Reporte');


-------------------------------
create table Rol(
ID serial PRIMARY KEY, --autoincremental
Nombre varchar(60) not null
);

select * from Rol;
insert into Rol(Nombre)values
('Admin'),
('Cajero'),
('Mesero');



-------------------------------
create table Privilegio_Rol(
ID_Privilegio integer not null,
ID_Rol integer not null,
primary key (ID_Privilegio,ID_Rol),
foreign key (ID_Privilegio) references Privilegio(ID)
on update cascade
on delete cascade,
foreign key (ID_Rol) references Rol(ID)
on update cascade
on delete cascade
);

-- solo estoy agregando al administrador 
select * from privilegio_rol;

insert into Privilegio_Rol(ID_Privilegio,ID_Rol)values
(1,1),
(2,1),
(3,1),
(4,1),
(5,1),
(6,1),
(7,1),
(8,1);


---------------------
create table Usuario(
ID serial PRIMARY KEY, --autoincremental
Nombre varchar(30) not null,
Contraseña varchar(150) not null,
ID_Rol int not null, 	 
Estado varchar(10) not null,

foreign key (ID_Rol) references Rol(ID)
on update cascade
on delete cascade
);
--usuario aministradores
select * from Usuario;

insert into Usuario (Nombre,Contraseña,ID_Rol,Estado)values
('franz','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',1,'activo'),
('mauricio','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',1,'activo'),
('jose','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',1,'activo'),
('edward','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',1,'activo'),
('yhoselihn','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',1,'activo'),
--update Usuario set Nombre = 'mauricio' where ID = 2

--usuario CaJERO
('sandra','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',2,'activo'),
('lola','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',2,'activo'),
('pedro','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',2,'activo'),

--usuario meseros

('leanne','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',3,'activo'),
('fatima','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',3,'activo'),
('lourdes','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',3,'activo'),
('yesmin','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',3,'activo'),
('nathaly','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',3,'activo'),
('yoana','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',3,'activo'),
('veronica','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',3,'activo'),
('katherin','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',3,'activo');

Create table Personal
(	ID serial PRIMARY KEY, --autoincremental
	Nombre varchar(40)not null,
    ApellidoP varchar(20) not null,
	ApellidoM varchar(20) ,
	Telefono varchar(10),
	CI varchar(20) not null,
    Correo varchar(50) not null,
	Fecha_Nacimiento date not null,
	ID_usuario int not null,
	foreign key (ID_usuario) references Usuario(ID)
	on update cascade
	on delete cascade
	
);


select * from personal;

--admin
insert into Personal (Nombre,ApellidoP,ApellidoM,Telefono,CI,Correo,Fecha_Nacimiento,ID_usuario) values
('FRANZ','RIBERA','SAAVEDRA','78596734','6012345 SCZ','ribera.franz@ficct.uagrm.edu.bo','1990-10-07',1),
('ROQUE MAURICIO','BANEGAS','LOPEZ','77316017','4512025 SCZ','poeta160886@gmail.com','1990-10-07',2),
('JOSE LUIS','RODRIGUEZ','VALENCIA','60947219','4512350 SCZ','jluisrv93@gmail.com','1990-10-07',3),
('JONATHAN EDWARD','GONZALES','PEÑAFIEL','60927522','1250316 SCZ','psicologo491@gmail.com','1990-10-07',4),
('YHOSELIHN AIDE','GOMEZ','ROCHA','65862565','9635412 SCZ','yhoselihnaidegomezr@gmail.com','1990-10-07',5),

-- Cajero
('Sandra', 'Tomicha', 'Rodriguez','798438','9635412 SCZ','Tomicha54@gmail.com','1996-06-15',6),
('Lola', 'Pacheco', 'Aldana','613114','9635412 SCZ','Pacheco53@gmail.com','1990-07-05',7),
('Pedro', 'Quevedo', 'Ribera','753534','9635412 SCZ','Quevedo47@gmail.com','1984-11-19',8),

--meseros
('Leanne Grace', 'Zurita', 'Frias','709920','9635412 SCZ','Zurita49@gmail.com','1980-05-10',9),
('Fatima', 'Ferrufino', 'Robles','634105','9635412 SCZ','Ferrufino46@gmail.com','1977-02-07',10),
('Lourdes Gerorgina', 'Garzón', 'Menacho','608678','9635412 SCZ','Garzon52@gmail.com','1991-05-11',11),
('Yesmin','Manjares',null,null,'9635412 SCZ','Manjares51@gmail.com','1995-05-14',12),
('Nathaly', 'Lazarte',null,null,'9635412 SCZ','Lazarte50@gmail.com','1991-12-25',13),
('Yoana', 'Vaca', 'Lopez','785955','9635412 SCZ','Vaca48@gmail.com','1989-01-20',14),
('Veronica', 'Carrizales', 'Tasima','609056','9635412 SCZ','Carrizales45@gmail.com','1994-11-04',15),
('Katherin', 'Arteaga', 'Melgar',null,'9635412 SCZ','Arteaga44@gmail.com','1990-10-07',16);

--realizar las demas tablas

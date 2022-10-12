create database DB_PostVenta;
use DB_PostVenta;




Create table Personal
(	CI integer not null,
	Nombre varchar(40)not null,
    ApellidoP varchar(15) not null,
	ApellidoM varchar(15) ,
	Telefono Decimal(10),
    Correo varchar(40),
	Fecha_Nacimiento date not null,
	primary key (CI)
);


select * from personal
-- Cajero
insert into personal values(1,'Sandra', 'Tomicha', 'Rodriguez',798438,'Tomicha54@virtual.com','1996-06-15');
insert into personal values(2,'Lola', 'Pacheco', 'Aldana',613114,'Pacheco53@virtual.com','1990-07-05');
insert into Personal values(3,'Pedro', 'Quevedo', 'Ribera',753534,'Quevedo47@virtual.com','1984-11-19');

--meseros
insert into personal values(4,'Leanne Grace', 'Zurita', 'Frias',709920,'Zurita49@virtual.com','1980-05-10');
insert into personal values(5,'Fatima', 'Ferrufino', 'Robles',634105,'Ferrufino46@virtual.com','1977-02-07');
insert into personal values(6,'Lourdes Gerorgina', 'Garzón', 'Menacho',608678,'Garzon52@virtual.com','1991-05-11');
insert into personal values(7,'Yesmin','Manjares',null,null,'Manjares51@virtual.com','1995-05-14');
insert into personal values(8,'Nathaly', 'Lazarte',null,null,'Lazarte50@virtual.com','1991-12-25');
insert into Personal values(9,'Yoana', 'Vaca', 'Lopez',785955,'Vaca48@virtual.com','1989-01-20');
insert into personal values(10,'Veronica', 'Carrizales', 'Tasima',609056,'Carrizales45@virtual.com','1994-11-04');
insert into Personal values(11,'Katherin', 'Arteaga', 'Melgar',null,'Arteaga44@virtual.com','1990-10-07');


--admin

insert into Personal values(12,'FRANZ','RIBERA','SAAVEDRA',78596734,'ribera.franz@ficct.uagrm.edu.bo','1990-10-07');



-------------------------------
create table Privilegio(
ID integer not null,
Descripcion varchar(60) not null,
primary key(ID)
);

select * from privilegio;

insert into Privilegio values(1,'Agregar Usuario');
insert into Privilegio values(2,'Actualizar Usuario');
insert into Privilegio values(3,'Eliminar Personal');
insert into Privilegio values(4,'Registrar Personal');
insert into Privilegio values(5,'Modificar Personal');
insert into Privilegio values(6,'Eliminar Personal');
insert into Privilegio values(7,'Registrar Reserva');
insert into Privilegio values(8,'Reporte');


-------------------------------
create table Rol(
ID integer not null,
Nombre varchar(60) not null,
primary key(ID)
);

select * from Rol;
insert into Rol values(1,'Admin');
insert into Rol values(2,'Cajero');
insert into Rol values(3,'Mesero');



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

insert into Privilegio_Rol values(1,1);
insert into Privilegio_Rol values(2,1);
insert into Privilegio_Rol values(3,1);
insert into Privilegio_Rol values(4,1);
insert into Privilegio_Rol values(5,1);
insert into Privilegio_Rol values(6,1);
insert into Privilegio_Rol values(7,1);
insert into Privilegio_Rol values(8,1);


---------------------
create table Usuario(
ID integer not null,
Nombre varchar(30) not null,
Contraseña varchar(150) not null,
ID_Rol integer not null, 	 
primary key (ID),
ID_persona integer not null, 
foreign key (ID_persona) references Personal(CI)
on update cascade
on delete cascade,
foreign key (ID_Rol) references Rol(ID)
on update cascade
on delete cascade
);
--- solo he agregado un usuario administrador
select * from Usuario;
insert into Usuario values(1,'franz','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',1,12);


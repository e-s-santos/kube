 create database mimosa; 
 use mimosa; 

 create table arquivo (arquivo varchar(255), email varchar(255), verif int);
 alter table arquivo add tif datetime;
 alter table arquivo add tii datetime;
 alter table arquivo add hostname varchar(100);
 
 
 create table proc (proc int, hostname nvarchar(100)) ;

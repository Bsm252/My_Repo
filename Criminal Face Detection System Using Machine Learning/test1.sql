create database test1;
use criminaldb;
create table criminaldata1(
id int primary key auto_increment,
`name` varchar(20) not null,
`father name` varchar(25),
`gender` varchar(6) not null,
`dob` varchar(10) not null,
`crimes` text not null);
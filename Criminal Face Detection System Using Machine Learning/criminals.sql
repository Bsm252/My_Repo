create database criminal;

use criminal;

create table criminals(
	id int primary key auto_increment,
    name varchar(255),
    father_name varchar(255),
    gender varchar(10),
    dob varchar(255),
    crimes_done varchar(255)
);

select * from criminals;

set sql_safe_updates = 0;

delete from criminals;
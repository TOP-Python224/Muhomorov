drop database if exists phonebook;

create database phonebook;
use phonebook;

create table people (
	`id` smallint unsigned not null auto_increment primary key,
    `full_name` varchar(50) not null unique,
    constraint `CH_people_full_name` check (`full_name` <> ''),
    `birth_date` date,
    `gender` enum('Male', 'Female'),
    `phone` varchar(16) not null unique,
    constraint `CH_people_phone` check (`phone` <> '' and `phone` rlike "^\\+?[0-9]{6,15}$"),
    `city` varchar(25),
    constraint `CH_people_city` check (`city` <> ''),
    `country` varchar(25) default 'Russia',
    constraint `CH_people_country` check (`country` <> ''),
    `address` varchar(25),
    constraint `CH_people_address` check (`address` <> '')
);
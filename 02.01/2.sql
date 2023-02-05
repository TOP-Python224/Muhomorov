drop database if exists sales_db;

create database sales_db;
use sales_db;

create table sellers (
	`id` tinyint unsigned not null auto_increment primary key,
    `full_name` varchar(50) not null unique,
    constraint `CH_sellers_full_name` check (`full_name` <> ''),
    `email` varchar(25) not null unique,
    constraint `CH_sellers_email` check (`email` <> '' and `email` like '%@%'),
    `phone` varchar(16) not null unique,
    constraint `CH_sellers_phone` check (`phone` <> '' and `phone` rlike "^\\+?[0-9]{6,15}$")
);

create table buyers (
	`id` tinyint unsigned not null auto_increment primary key,
    `full_name` varchar(50) not null unique,
    constraint `CH_buyers_full_name` check (`full_name` <> ''),
    `email` varchar(25) not null unique,
    constraint `CH_buyers_email` check (`email` <> '' and `email` like '%@%'),
    `phone` varchar(16) not null unique,
    constraint `CH_buyers_phone` check (`phone` <> '' and `phone` rlike "^\\+?[0-9]{6,15}$")
);

create table sales (
	`id` tinyint unsigned not null auto_increment primary key,
    `seller_id` tinyint unsigned not null,
    `buyer_id` tinyint unsigned not null,
    `goods` varchar(50) not null,
    constraint `CH_sales_goods` check (`goods` <> ''),
    `price` decimal(9, 2) not null,
    constraint `CH_sales_price` check (`price` > 0),
    `date` date not null
);

alter table sales 
	add constraint `FK_sales_seller_id`
		foreign key (`seller_id`)
		references sellers (`id`),
	add constraint `FK_sales_buyer_id`
		foreign key (`buyer_id`)
        references buyers (`id`);
       

    




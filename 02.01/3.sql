-- Немного отступил от ТЗ, т.к. хранить данные о диске и исполнителе в песне не очень логично: песня привязывается одному диску и к одному исполнителю,
-- поэтому использовал связь многие-ко-многим между песня - диск и песня - исполнитель.

drop database if exists music;

create database music;
use music;

create table disks (
	`id` smallint unsigned not null	auto_increment primary key,
    `name` varchar(25) not null unique,
    constraint `CH_dicks_name` check (`name` <> ''),
    `singer` smallint not null,
    `date` date not null,
    `style` tinyint not null,
    `publisher` tinyint unsigned not null
);

create table styles(
	`id` tinyint not null auto_increment primary key,
    `name` enum ('rock', 'pop', 'rap', 'heavy', 'classic', 'collection', 'other')
);

create table singers (
	`id` smallint not null auto_increment primary key,
    `name` varchar(25) not null unique,
    constraint `CH_singers_name` check (`name` <> '')
);

create table publishers (
	`id` tinyint unsigned not null auto_increment primary key,
    `name` varchar(25) not null unique,
    constraint `CH_publishers_name` check (`name` <> ''),
    `country` varchar(25) not null,
    constraint `CH_publishers_country` check (`country` <> '')
);

create table songs (
	`id` smallint unsigned not null auto_increment primary key,
    `name` varchar(25) not null,
    constraint `CH_songs_name` check (`name` <> ''),
    `length` tinyint not null,
    constraint `CH_songs_length` check (`length` > 0),
    `style` tinyint not null
);

create table songs_disks (
	`song_id` smallint unsigned not null,
    `disk_id` smallint unsigned not null,
    constraint primary key (`song_id`, `disk_id`)
);

create table singers_songs (
	`singer_id` smallint not null,
    `song_id` smallint unsigned not null,
    constraint primary key (`singer_id`, `song_id`)
);

alter table disks
	add constraint `FK_disks_singer`
		foreign key (`singer`)
        references singers (`id`),
	add constraint `FK_disks_style`
		foreign key (`style`)
        references styles (`id`),
	add constraint `FK_disks_publisher`
		foreign key (`publisher`)
        references publishers (`id`);
        
alter table songs
	add constraint `FK_songs_style`
		foreign key (`style`)
        references styles (`id`);
        
alter table songs_disks
	add constraint `FK_songs_disks_song_id`
    foreign key (`song_id`)
    references songs (`id`),
    add constraint `FK_songs_disks_disk_id`
	foreign key (`disk_id`)
    references disks (`id`);
    
alter table singers_songs
	add constraint `FK singers_songs_singer_id`
    foreign key (`singer_id`)
    references singers (`id`),
    add constraint `FK singers_songs_song_id`
    foreign key (`song_id`)
    references songs (`id`);
    
alter table disks
	add column `review` varchar(100);
    
alter table publishers
	add column `address` varchar(50) not null;

alter table disks
	drop column `review`;

alter table publishers
	drop column `address`;
    
create view all_styles
	as select name from styles;

create view all_publishers
	as select name from publishers;

create view disk_info
	as select * from disks where disks.`id` = 1;
 

    


 
     

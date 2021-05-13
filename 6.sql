create table if not exists Genre ( 
	GenreID serial primary key,
	Name varchar(50) not null
);
create table if not exists Author (
	AuthorID serial primary key,
	Name varchar(100) not null
);
create table if not exists Genre_Author (
	AuthorID integer references Author(AuthorID),
	GenreID integer references Genre(GenreID),
	constraint Genre_Author_pk primary key (AuthorID, GenreID)
);
create table if not exists Album (
	AlbumID serial primary key,
	Name varchar(100) not null,
	Year integer
);
create table if not exists Feat (
	AuthorID integer references Author(AuthorID), 
	AlbumID integer references Album(AlbumID), 
	constraint Feat_pk primary key (AuthorID, AlbumID)
);
create table if not exists Song (
	SongID serial primary key,
	AlbumID integer references Album(AlbumID), 
	Name varchar(100) not null,
	Duration_sec integer
);
create table if not exists Collection ( 
	CollectionID serial primary key,
	Name varchar(100) not null,
	Year integer
);
create table if not exists Song_Collection (
	SongID integer references Author(AuthorID),
	CollectionID integer references Album(AlbumID),
	constraint Song_Collection_pk primary key (SongID, CollectionID)
);
create table if not exists genres (
	id serial primary key,
	genre_title varchar(40) not null unique
);

create table if not exists singers (
	id serial primary key,
	singer_name varchar(40) not null
);

create table if not exists GenresSingers (
	singer_id integer references singers(id),
	genre_id integer references genres(id),
	constraint p_key_GSing primary key (genre_id, singer_id)
);

create table if not exists albums (
	id serial primary key,
	album_title varchar(40) not null,
	release_year integer not null
);

create table if not exists SingersAlbums (
	singer_id integer references singers(id),
	album_id integer references albums(id),
	constraint p_key_SingAlb primary key (singer_id, album_id)
);

create table if not exists tracks (
	id serial primary key,
	track_title varchar(40) not null unique,
	duration real not null,
	album_id integer references albums(id)
);

create table if not exists collection (
	id serial primary key,
	col_title varchar(40) not null,
	release_year integer not null
);

create table if not exists TracksCollection (
	track_id integer references tracks(id),
	col_id integer references collection(id),
	constraint p_key_TCol primary key (col_id, track_id)
);
-- for experimenting
DROP DATABASE IF EXISTS engl_games;

CREATE DATABASE engl_games;

\connect engl_games

CREATE TABLE player (
    id serial primary key,
    nick varchar(20) not null default 'Player',
    last_activity date not null default now()
);

CREATE TABLE room (
    id serial primary key,
    code uuid not null,
    owner_id integer unique references player(id) on delete cascade
);

CREATE TABLE room_players (
    id serial primary key,
    player_id integer unique references player(id) on delete cascade,
    room_id integer references room(id) on delete cascade
);

CREATE TABLE game (
    id serial primary key,
    creation_time timestamp not null,
    theme varchar(20) not null default 'all',
    duration interval not null default '5 minutes',
    template varchar(20) not null default 'basic',
    image_url text,
    room_id integer unique references room(id) on delete cascade
);

-- CREATE TABLE gallary (
--     id integer primary key,
--     nick varchar(20) not null,
--     art text not null,
--     date date not null
-- );
-- for experimenting
DROP DATABASE IF EXISTS engl_games;

CREATE DATABASE engl_games;

\connect engl_games

CREATE TABLE player (
    id integer primary key,
    nick varchar(20) not null default 'Player'
    -- conn text not null,
);

CREATE TABLE game (
    id integer primary key,
    creation_time timestamp not null,
    theme varchar(20) not null default 'all',
    duration interval not null default '5 minutes',
    template varchar(20) not null default 'basic',
    image_url text,
    narrator_id integer references player(id)
);

CREATE TABLE game_players (
    id integer primary key,
    player_id integer references player(id),
    game_id integer references game(id)
);

CREATE TABLE gallary (
    id integer primary key,
    nick varchar(20) not null,
    art text not null,
    date date not null
);
\connect engl_games

DELETE FROM player;
DELETE FROM room;
DELETE FROM room_players;
DELETE FROM game;

INSERT INTO player VALUES 
    (1, 'Bob', DEFAULT),
    (2, DEFAULT, DEFAULT),
    (3, 'King Kong', DEFAULT),
    (4, 'Avatar', DEFAULT);

INSERT INTO room VALUES
    (1, 'd90271f2-3ada-4f67-9e17-7676836e1dd7', 1),
    (2, 'a089a57d-0e0f-4efc-8033-d34eff98623e', 2);

INSERT INTO room_players VALUES
    (DEFAULT, 1, 1),
    (DEFAULT, 2, 2),
    (DEFAULT, 3, 1),
    (DEFAULT, 4, 1);

INSERT INTO game VALUES
    (DEFAULT, '2021-05-20 12:05:05', 'anime', '6 minutes', 'manga', 'img url', 1),
    (DEFAULT, '2021-05-20 12:05:05', DEFAULT, DEFAULT, DEFAULT, 'img url', 2);

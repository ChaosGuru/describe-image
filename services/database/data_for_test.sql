\connect engl_games

INSERT INTO player VALUES 
    (DEFAULT, 'Bob'),
    (DEFAULT, DEFAULT),
    (DEFAULT, 'King Kong'),
    (DEFAULT, 'Avatar');

INSERT INTO game VALUES
    (DEFAULT, '2021-05-20 12:05:05', 'anime', '6 minutes', 'manga', 'img url', 1),
    (DEFAULT, '2021-05-20 12:05:05', DEFAULT, DEFAULT, DEFAULT, 'img url', 3);

INSERT INTO game_players VALUES
    (DEFAULT, 1, 1),
    (DEFAULT, 2, 1),
    (DEFAULT, 3, 2),
    (DEFAULT, 4, 2);
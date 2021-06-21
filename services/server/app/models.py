from .db import Base


class Player(Base):
    __table__ = Base.metadata.tables['player']


class Game(Base):
    __table__ = Base.metadata.tables['game']


class GamePlayers(Base):
    __table__ = Base.metadata.tables['game_players']
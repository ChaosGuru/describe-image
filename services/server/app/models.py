from .db import Base
from sqlalchemy.orm import relationship


class Player(Base):
    __table__ = Base.metadata.tables['player']


class Game(Base):
    __table__ = Base.metadata.tables['game']


class GamePlayers(Base):
    __table__ = Base.metadata.tables['game_players']
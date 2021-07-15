from .db import Base
from sqlalchemy.orm import relationship


class Player(Base):
    __table__ = Base.metadata.tables['player']

class Room(Base):
    __table__ = Base.metadata.tables['room']

class RoomPlayers(Base):
    __table__ = Base.metadata.tables['room_players']

class Game(Base):
    __table__ = Base.metadata.tables['game']
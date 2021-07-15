from flask import Blueprint, render_template_string, jsonify

from .models import Player, Game, RoomPlayers, Room
from .db import db_session


api_bp = Blueprint('api', __name__, subdomain="api")


@api_bp.route('/test')
def test_db():
    players = db_session.query(
        Player.id, 
        Player.nick, 
        Player.last_activity
    ).all()

    rooms = db_session.query(
        Room.id,
        Room.code,
        Room.owner_id,
        Player.nick
    ).join(Player).all()

    games = db_session.query(
        Game.id,
        Game.creation_time,
        Game.template,
        Room.code
    ).join(Room).all()

    return "{}{}{}".format(players, rooms, games)


# get player
# get game
# get game participants


# create player
# create game
# create game participants


# delete player
# delete game # and participants (add on delete to sql)
# delete game participants


# update player
# update game
# update game participants
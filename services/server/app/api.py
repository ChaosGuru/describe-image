from flask import Blueprint, render_template_string

from .models import Player, Game, GamePlayers
from .db import db_session


api_bp = Blueprint('api', __name__, subdomain="api")


@api_bp.route('/test')
def test_bp():
    # all players
    players = db_session.query(Player.id, Player.nick)

    # all games
    games = db_session.query(
        Game.id,
        Game.creation_time,
        Game.theme,
        Game.duration,
        Game.template,
        Game.image_url,
        Player.id,
        Player.nick).join(Player)

    # all players and their games (join)
    game_players = db_session.query(
        GamePlayers.id,
        Player.id, 
        Player.nick,
        Game.id,
        Game.creation_time).select_from(GamePlayers).join(Player, Game)
    
    return render_template_string("""
        <h1>players:</h1>
        <table>
            <thead>
                <th>id</th>
                <th>nick</th>
            </thead>
            <tbody>
            {% for pl in players %}
                <tr>
                    <td>{{ pl[0] }}</td>
                    <td>{{ pl[1] }}</td>
                </tr>
            {% endfor %}
            </tbody>
        </table>
        <br>
        <table>
            <thead>
                <th>id</th>
                <th>timestamp</th>
                <th>theme</th>
                <th>duration</th>
                <th>template</th>
                <th>image</th>
                <th>player id</th>
                <th>player</th>
            </thead>
            <tbody>
            {% for gm in games %}
                <tr>
                    <td>{{ gm[0] }}</td>
                    <td>{{ gm[1] }}</td>
                    <td>{{ gm[2] }}</td>
                    <td>{{ gm[3] }}</td>
                    <td>{{ gm[4] }}</td>
                    <td>{{ gm[5] }}</td>
                    <td>{{ gm[6] }}</td>
                    <td>{{ gm[7] }}</td>
                </tr>
            {% endfor %}
            </tbody>
        </table>
        <br>
        <table>
            <thead>
                <th>id</th>
                <th>player id</th>
                <th>player</th>
                <th>game id</th>
                <th>game creation</th>
            </thead>
            <tbody>
            {% for pl in game_players %}
                <tr>
                    <td>{{ pl[0] }}</td>
                    <td>{{ pl[1] }}</td>
                    <td>{{ pl[2] }}</td>
                    <td>{{ pl[3] }}</td>
                    <td>{{ pl[4] }}</td>
                </tr>
            {% endfor %}
            </tbody>
        </table>
    """, players=players, games=games, game_players=game_players)


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
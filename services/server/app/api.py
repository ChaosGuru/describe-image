from flask import Blueprint, render_template_string

from .models import Player
from .db import db_session


api_bp = Blueprint('api', __name__, subdomain="api")


@api_bp.route('/')
def test_bp():
    players = db_session.query(Player.id, Player.nick)

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
    """, players=players)
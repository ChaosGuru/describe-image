from flask import Flask

from .api import api_bp

app = Flask(__name__)

# change in production
app.config['SERVER_NAME'] = 'localhost:5000'

app.register_blueprint(api_bp)
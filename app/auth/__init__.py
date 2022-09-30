# authentication blueprint

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import login_views
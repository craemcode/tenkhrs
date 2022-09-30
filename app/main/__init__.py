# here we have the blueprint. this is where the routes and custom pages(decorators for app)
# are created..the blueprint is an app. we initialize it here so it can be executed before the
# package starts existing.


from flask import Blueprint

main = Blueprint('main', __name__)

# importing the routes makes them associated with the blueprint. they are
# imported at the bottom to avoid circular imports error.
from . import controllers

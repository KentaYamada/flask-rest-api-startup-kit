from flask import json, Flask
from werkzeug.exceptions import HTTPException


app = Flask(__name__)


# register error handler
@app.errorhandler(HTTPException)
def handle_api_exception(e):
    """ return JSON instead of HTML for HTTP errors. """
    response = e.get_response()
    response.content_type = 'application/json'
    data = json.dumps({
        'code': e.code,
        'description': e.description
    })
    response.set_data(data)
    return response

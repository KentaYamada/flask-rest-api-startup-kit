from flask import jsonify, request, Blueprint
from werkzeug.exceptions import BadRequest, NotFound
from app.libs.json_response import Created, NoContent, OK


sample_api = Blueprint('sample', __name__, url_prefix='/api/samples')
languages = [
    {'id': 1, 'language': 'python'},
    {'id': 2, 'language': 'rust'},
    {'id': 3, 'language': 'javascript'},
    {'id': 4, 'language': 'c'}
]

@sample_api.route('/', methods=['GET'])
def get():
    return OK({'message': 'ham'})


@sample_api.route('/<int:id>', methods=['GET'])
def get_by_language(id):
    data = next((l for l in languages if id == l['id']), None)
    if data is None:
        raise NotFound(description='Language not found')
    return OK(data)


@sample_api.route('/', methods=['POST'])
def post():
    payload = request.get_json()
    if payload is None:
        raise BadRequest(description='Request has no data')
    whitelist = {'language'}
    if not payload.keys() >= whitelist:
        raise BadRequest(description='Invalid request')
    lastRow = languages[-1]
    data = {'id': lastRow['id'] + 1, 'language': payload['language']}
    languages.append(data)
    return Created(data)


@sample_api.route('/<int:id>', methods=['PUT'])
def put(id):
    payload = request.get_json()
    whitelist = {'language'}
    if not payload.keys() >= whitelist:
        raise BadRequest(description='Invalid request')
    for l in languages:
        if l['id'] == id:
            l['language'] = payload['language']
            return OK(l)
    raise NotFound(description='Language is not exist')

@sample_api.route('/<int:id>', methods=['DELETE'])
def delete(id):
    for i, l in enumerate(languages):
        if l['id'] == id:
            return NoContent()
    raise NotFound(description='Language is not exist')

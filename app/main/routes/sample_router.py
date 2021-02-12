from flask import Blueprint, jsonify, request

sample = Blueprint('sample', __name__, url_prefix='/sample')


@sample.route('/', methods=['GET'])
def update_movie():
    return jsonify({
        "code": 1,
        "data": "sample"
    })
from flask import Flask, request, jsonify, Blueprint
from marshmallow import ValidationError

from db import db
from make_query import build_query
from model import PackageRequestSchema

main_bp = Blueprint('main', __name__)

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DATA_DIR = os.path.join(BASE_DIR, "data")
file_name = "data/apache_logs.txt"


@main_bp.route("/perform_query", methods=['POST'])
def perform_query():
    query_data = request.json
    try:
        validated_data = PackageRequestSchema().load(query_data)

    except ValidationError as error:
        return jsonify(error.messages), 400

    result = None
    for query in validated_data['queries']:
        result = build_query(
            cmd=query['cmd'],
            value=query['value'],
            file_name=validated_data['file_name'],
            data=result
        )

    return jsonify(result)


@main_bp.route("/ping", methods=['GET'])
def ping():
    return 'pong'


@main_bp.route("/test_db", methods=['GET'])
def test_db():
    result = db.session.execute(
        """
        SELECT 1;
        """
    ).scalar()
    return jsonify({'result': result})

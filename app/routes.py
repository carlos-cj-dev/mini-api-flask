from flask import Blueprint, request, jsonify
from app.models import db, User
from sqlalchemy import text
from app.service import create_user_service, update_user_service

urls = Blueprint('url', __name__)

@urls.route('/api')
def welcome():
    return "Welcome to the Flask Application!"


@urls.post("/api/users")
def create_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    
    result, status_code = create_user_service(name, email)
    return jsonify(result), status_code

@urls.put("/api/users/<int:user_id>")
def update_user(user_id):
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    
    result, status_code = update_user_service(user_id, name, email)
    return jsonify(result), status_code





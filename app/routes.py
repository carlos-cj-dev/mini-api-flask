from flask import Blueprint, request, jsonify
from app.models import db, User
from sqlalchemy import text

urls = Blueprint('url', __name__)

@urls.route('/api')
def welcome():
    return "Welcome to the Flask Application!"


@urls.post("/api/users")
def create_user():
    data = request.get_json()
    name=data.get("name")
    email=data.get("email")

    if not email or not name:
        return jsonify({"error": "Missing 'email' or 'name'"}), 400

    exist_user = db.session.execute(
        text("SELECT * FROM user WHERE email = :email"),
        {"email": email}
    ).fetchone()

    if(exist_user):
        return jsonify({"error": "User already exsit"}), 400

    
    new_user = User(
        name=name,
        email=email
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "User created successfully",
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email
        }
    }), 201






from app.models import db, User
from sqlalchemy import text


def create_user_service(name, email):
    if not email or not name:
        return {"error": "Missing 'email' or 'name'"}, 400

    exist_user = db.session.execute(
        text("SELECT * FROM user WHERE email = :email"),
        {"email": email}
    ).fetchone()

    if exist_user:
        return {"error": "User already exist"}, 400

    new_user = User(
        name=name,
        email=email
    )

    db.session.add(new_user)
    db.session.commit()

    return {
        "message": "User created successfully",
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email
        }
    }, 201


def update_user_service(user_id, name, email):
    if not user_id:
        return {"error": "Id do usuário é obrigatório"}, 400
    
    if not name and not email:
        return {"error": "Pelo menos o nome ou email deve ser fornecido"}, 400
    
    user = db.session.execute(
        text("SELECT * FROM user WHERE id = :id"),
        {"id": user_id}
    ).fetchone()
    
    if not user:
        return {"error": "Usuário não encontrado"}, 404
    
    if email:
        existing_email = db.session.execute(
            text("SELECT * FROM user WHERE email = :email AND id != :id"),
            {"email": email, "id": user_id}
        ).fetchone()
        
        if existing_email:
            return {"error": "Email já está em uso por outro usuário"}, 400
    
    user_obj = db.session.get(User, user_id)
    
    if name:
        user_obj.name = name
    if email:
        user_obj.email = email
    
    db.session.commit()
    
    return {
        "message": "Usuário atualizado com sucesso",
        "user": {
            "id": user_obj.id,
            "name": user_obj.name,
            "email": user_obj.email
        }
    }, 200


import uuid
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash
from peewee import IntegrityError
from infrastructure.db.models.user_model import UserModel
from core.exceptions.exceptions import UserNotFoundException, get_user_or_raise

def create_app():
    load_dotenv()
    app = Flask(__name__)

    @app.errorhandler(UserNotFoundException)
    def handle_user_not_found(error):
        return jsonify({"error": error.message}), 404


    @app.route("/users", methods=["POST"])
    def create_user():
        data = request.get_json()
        if not data or "username" not in data or "password" not in data or "person_id" not in data:
            return jsonify({"error": "Formato de solicitud no válido!"}), 400

        hashed_password = generate_password_hash(data["password"])
        try:
            user = UserModel.create(
                id=uuid.uuid4(),
                username=data["username"].lower(),  # Aquí se normaliza a minúsculas
                password=hashed_password,
                person_id=data["person_id"],
                activated=True,
                date_created=datetime.utcnow(),
                date_modified=datetime.utcnow()
            )
            return jsonify({"message": "Usuario creado correctamente!", "user_id": str(user.id)}), 201
        except IntegrityError:
            return jsonify({"error": "Username or person_id ya exísten!"}), 400


    @app.route("/users/<user_id>", methods=["GET"])
    def get_user(user_id):
        """Obtiene un usuario por ID"""
        try:
            user = get_user_or_raise(UserModel, user_id)
            return jsonify({
                "id": str(user.id),
                "username": user.username,
                "person_id": str(user.person_id),
                "activated": user.activated,
                "date_created": user.date_created,
                "date_modified": user.date_modified
            }), 200
        except UserNotFoundException:
            return jsonify({"error": "Usuario no encontrado"}), 404


    @app.route("/users/<user_id>", methods=["PUT"])
    def update_user(user_id):
        data = request.get_json()
        if not data:
            return jsonify({"error": "Formato de solicitud no válido!"}), 400

        user = get_user_or_raise(UserModel, user_id)
        user.username = data.get("username", user.username)
        user.password = generate_password_hash(data["password"]) if "password" in data else user.password
        user.person_id = data.get("person_id", user.person_id)
        user.activated = data.get("activated", user.activated)
        user.date_modified = datetime.utcnow()
        user.save()

        return jsonify({"message": "Usuario actualizado correctamente!"}), 200


    @app.route("/users/<user_id>", methods=["DELETE"])
    def delete_user(user_id):
        user = get_user_or_raise(UserModel, user_id)
        user.delete_instance()
        return jsonify({"message": "Usuario eliminado correctamente!"}), 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')

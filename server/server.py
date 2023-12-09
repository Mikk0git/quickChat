from app import app, db, DB_NAME
from os import path
from models import User, Message, Room
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash


def create_database():
    if not path.exists("db/" + DB_NAME):
        with app.app_context():
            db.create_all()
            print("Database created")


@app.route("/create-room", methods=["POST"])
def create_room():
    data = request.get_json()
    new_room = Room(id = data['id'], password=generate_password_hash(data['password'], method="pbkdf2:sha256"))
    db.session.add(new_room)
    db.session.commit()
    

    print("New room created ID: " +data['id'])

    return jsonify(data), 201

@app.route("/get-messages/<room_id>")
def get_messages(room_id):
    messages = {
        "message1" : {
            "text" : "dupa123",
            "senderId" : "20133"
        }
    }

    return jsonify(messages), 200


@app.route("/send-message", methods=["POST"])
def send_message():
    data = request.get_json()

    print(data)

    return jsonify(data), 201


if __name__ == "__main__":
    create_database()
    app.run(debug=True)
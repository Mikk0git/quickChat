from app import app, db, DB_NAME
from os import path
from models import User, Message, Room
from flask import request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash


def create_database():
    if not path.exists("instance/" + DB_NAME):
        with app.app_context():
            db.create_all()
            print("Database created")


@app.route("/create-room", methods=["POST"])
def create_room():
    data = request.get_json()
    if data['password'] == "":
        password = "1"
    else:
        password = data['password']
    new_room = Room(id = data['id'], password=generate_password_hash(password, method="pbkdf2:sha256"))
    db.session.add(new_room)

    create_user(data["username"])
    connect_user_to_room(data["username"],data["id"])
    
    room = db.session.get(Room, data['id'])
    if room:
        print("Room created ID: " +data['id'])
        return jsonify({"message": "Room created ID: " +data['id']}), 200
    else:
        return jsonify({"message": "Room creation failed"}), 500


def create_user(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        user = User(username= username)
        db.session.add(user)
        db.session.commit()
        print(f"New user added {username}")


def connect_user_to_room(username, roomId):
    user = User.query.filter_by(username=username).first()
    room = db.session.get(Room, roomId)
    if user and room:
        user.rooms.append(room)
        db.session.commit()
        print(f"Connected user {username} to room {roomId}")
    

@app.route("/get-messages/<room_id>")
def get_messages(room_id):
    messages =  Message.query.filter_by(roomId=room_id).all()

    formatted_messages = {}
    for message in messages:
        formatted_messages[message.id] = {
            "text": message.content,
            "userId": message.userId,
            "date": message.date
        }

    return jsonify(formatted_messages), 200


@app.route("/send-message", methods=["POST"])
def send_message():
    data = request.get_json()

    new_message = Message(content = data['content'], userId = data["userId"], roomId = data["roomId"])
    db.session.add(new_message)
    db.session.commit()

    print("New message sent to room "+ data["roomId"] + " from " + data["userId"])

    return jsonify(data), 201


if __name__ == "__main__":
    create_database()
    app.run(debug=True)
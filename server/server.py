from flask import Flask, request, jsonify

app = Flask(__name__)


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
    app.run(debug=True)
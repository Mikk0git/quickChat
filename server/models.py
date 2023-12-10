from app import db
from sqlalchemy.sql import func

user_room = db.Table('user_room',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('room_id', db.String, db.ForeignKey('room.id'), primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    rooms = db.relationship('Room', secondary=user_room, backref='users')
    # messages = db.relationship('Message')

class Room(db.Model):
    id = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    messages = db.relationship('Message')

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    roomId = db.Column(db.String, db.ForeignKey('room.id'))

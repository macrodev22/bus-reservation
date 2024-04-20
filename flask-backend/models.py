from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=True)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number_of_passengers = db.Column(db.Integer, nullable=False)
    origin = db.Column(db.ForeignKey('city.id'), nullable=False)
    destination = db.Column(db.ForeignKey('city.id'), nullable=False)
    passengers = db.relationship('Passenger', backref='reservation', lazy=True)

    def __repr__(self) -> str:
        return f"{self.id} -> {self.number_of_passengers} pax"
    
class Passenger(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer)
    reservation_id = db.Column(db.ForeignKey('reservation.id'), nullable=False)


class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(10), nullable=False)

    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)

class Fare(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    origin = db.Column(db.ForeignKey('city.id'), nullable=False)
    destination = db.Column(db.ForeignKey('city.id'), nullable=False)
    amount = db.Column(db.Integer)

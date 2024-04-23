from flask_restful import Resource
from flask import request
from models import db, City, Reservation, Passenger, User, Fare
import bcrypt
from datetime import datetime
from auth_middleware import token_required
import bcrypt
import jwt
from dotenv import load_dotenv
import os

load_dotenv()
JWT_SECRET = os.getenv('JWT_SECRET')
JWT_ALGO = os.getenv('JWT_ALGO')


class CityResource(Resource):
    def get(self, city_id):
        result = City.query.filter_by(id=city_id).first()
        if result:
            return {
                'status': 'success',
                'city_id': result.id,
                'name': result.name
            }, 200
        else:
            return {
                'status': 'failed',
                'message' : 'No city found'
            }, 404
        


class CityListResource(Resource):
        def get(self):
             results = City.query.all()

             return [{
                'city_id': x.id,
                'name': x.name
            } for x in results]
        def post(self):
            data = request.json()

            new_city = City(name=data['name'], country=data['country'])
            return {
                'status': 'success'
            }


        
class ReservationListResource(Resource):
    @token_required
    def get(self, current_user):
        reservations = Reservation.query.all()

        results = []

        #Get Passengers
        for reservation in reservations:
            passenger_names = [ passenger.name for passenger in reservation.passengers ]
            origin = City.query.filter_by(id=reservation.origin).first()
            destination = City.query.filter_by(id=reservation.destination).first()
            results.append({
                "reservation_id": reservation.id,
                'number_of_passengers': reservation.number_of_passengers,
                'origin': origin.name,
                'destination': destination.name,
                'passengers': passenger_names
            })

        return { 
             "status": "success",
                "results": results
            }, 200
    
    def post(self):
        data = request.json

        passenger_names = data.get('passengers', [])
        origin = data['origin']
        destination = data['destination']

        # Creating a new reservation
        reservation = Reservation(number_of_passengers=len(passenger_names), origin=origin, destination=destination)
        db.session.add(reservation)
        db.session.commit()

        # Create passengers and add them to DB
        for passenger in passenger_names:
            passenger_record = Passenger(name=passenger, reservation=reservation, age=18)
            db.session.add(passenger_record)
        db.session.commit()

        return {
            "status" : "success",
            "message" : "Reservation created successfully",
            "data": {
                "reservation" : reservation.id,
                "passengers": passenger_names
            }
        }, 201
    
class ReservationResource(Resource):
    def get(self, reservation_id):
        result: Reservation = Reservation.query.filter_by(id = reservation_id).first()

        if(result):
            origin : City = City.query.filter_by(id=result.origin).first()
            destination : City = City.query.filter_by(id=result.destination).first()

            return {
                "status" : "success",
                "reservation_id" : result.id,
                'number_of_passengers': result.number_of_passengers,
                'origin': origin.name,
                'destination': destination.name
            }, 200
        else:
            return {
                "status": "fail",
                "message" : "No reservation found"
            }, 404
    
    @token_required
    def delete(self, current_user, reservation_id):
        result: Reservation = Reservation.query.filter_by(id=reservation_id).first()

        if not result:
            return {
                'status': 'fail',
                'message': 'record doen not exits'
            }, 400

        # Delete passengers associated to reservation
        Passenger.query.filter_by(reservation_id=reservation_id).delete()

        db.session.delete(result)

        db.session.commit()

        return {
            'status': 'success',
            'message': 'Test delete endpoint good',
            'data': {
                'id': reservation_id
            }
        }, 203

class UserListResource(Resource):
    def get(self):
        results = User.query.all()
        return {
            "status": 'success',
            'results': [{
                'id': x.id,
                'username': x.username,
                'fullname': x.fullname,

            } for x in results]
        }
    
    def post(self):
        req_body = request.json

        user = req_body.get('data', None)
        if user:
            if 'password' in user:
                password_hash = bcrypt.hashpw(user['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                #Convert date to object
                date = datetime.strptime(user['dateOfBirth'], '%Y-%m-%d')
                new_user = User(fullname=user['fullname'], username=user['username'], date_of_birth=date, password_hash=password_hash)
                db.session.add(new_user)
                db.session.commit()
                return {
                    'status': 'success',
                    'message': 'User added'
                }, 201
            else:
                return {
                    'status': 'fail',
                    'message': 'No password provided'
                }
            
        else:
            return {
                'status': 'fail',
                'message': 'No user in data'
            }, 400

class FareListResource(Resource):
    def get(self):
        results = Fare.query.all()

        return {
            'status': 'success',
            'results': [
            {
                'id': x.id,
                'origin': x.origin,
                'destination': x.destination,
                'amount': x.amount
            } for x in results
        ]
        }, 200

    @token_required
    def post(self, current_user):
        req_body = request.json
        origin = req_body['data'].get('origin')
        destination = req_body['data'].get('destination')
        fare = req_body['data'].get('fare')
        if not origin or not destination:
            return {
                'status': 'fail',
                'message': 'invalid origin or destination'
            }, 400
        
        new_fare = Fare(origin=origin, destination=destination, amount=fare)
        db.session.add(new_fare)
        db.session.commit()

        return {
            'status': 'success',
            'message': 'Fare updated successfully'
        }, 201
    
class FareCalcResource(Resource):
    def get(self, origin, destination):
        result: Fare = Fare.query.filter_by(origin=origin, destination=destination).first()
        if not result:
            return {
                "fare": 0,
                'origin': origin,
                'destination': destination
            }, 200
        
        return {
            'id': result.id,
            'fare': result.amount,
            'origin': result.origin,
            'destination': result.destination
        }

    
class AuthResource(Resource):
    def post(self):
        req_body = request.json
        username = req_body.get('username')
        password = req_body.get('password')

        user = User.query.filter_by(username=username).first()

        if not user:
            return {
                'status': 'fail',
                'message': 'User invalid',
                'error': 'unauthorized'
            }
        if bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
            token = jwt.encode(
                { 'user_id': user.id },
                JWT_SECRET,
                JWT_ALGO
            )
            return {
                'status': 'success',
                'token': token
            }, 200
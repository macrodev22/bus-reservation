from flask import Flask, render_template
from flask_cors import CORS
import jwt
from flask_restful import Api
from api.resources import CityResource, CityListResource, ReservationResource, ReservationListResource, UserListResource, FareListResource, FareCalcResource, AuthResource
from models import db

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SECRET_KEY'] = 'de550e7c-6072-485e-9f50-4e611337db21'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)


api.add_resource(CityListResource, '/api/cities', '/api/cities/')
api.add_resource(CityResource, '/api/cities/<int:city_id>')
api.add_resource(ReservationListResource, '/api/reservations', '/api/reservations/')
api.add_resource(ReservationResource, '/api/reservations/<int:reservation_id>')
api.add_resource(UserListResource, '/api/users', '/api/users/')
api.add_resource(FareListResource, '/api/fares', '/api/fares/')
api.add_resource(FareCalcResource, '/api/fares/<int:origin>/<int:destination>')
api.add_resource(AuthResource, '/api/login', '/api/login/')

@app.route("/")
def home():
    return render_template('index.html')

# Disable 
reinitialize_DB = True

if __name__ == '__main__':
    #OPTIONAL
    if reinitialize_DB:
        with app.app_context():
            db.create_all()
    app.run(debug=True)
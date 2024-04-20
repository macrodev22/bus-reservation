from flask import request, abort
import jwt
from dotenv import load_dotenv
import os
from functools import wraps
from models import User

# Load env
load_dotenv()
JWT_SECRET = os.getenv('JWT_SECRET')
JWT_ALGO = os.getenv('JWT_ALGO')

def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers['Authorization'].split(' ')[1]
        if not token:
            return {
                'status': 'fail',
                'message': 'Authorization token missing!',
                'error': 'Unauthorized'
            }, 401
        
        try:
            data = jwt.decode(token, JWT_SECRET, JWT_ALGO)
            user_id = data.get('user_id')
            current_user = User.query.get(user_id)

            if current_user is None:
                return {
                    'status': 'fail',
                    'message': 'Invalid authorization token',
                    'error': 'Unauthorized'
                }, 401
        except Exception as e:
            return {
                'status': 'fail',
                'message': 'Something went wrong',
                'error': str(e)
            }, 500
        
        return f(current_user, *args, **kwargs)
    return wrapper



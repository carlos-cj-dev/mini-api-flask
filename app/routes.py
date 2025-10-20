from flask import Blueprint


urls = Blueprint('api', __name__)

@urls.route('/')
def welcome():
    return "Welcome to the Flask Application!"








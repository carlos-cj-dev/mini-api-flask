from flask import Flask
from app.models import db
from app.models import User
from app.routes import urls



app = Flask(__name__)
app.register_blueprint(urls)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
db.init_app(app)


with app.app_context():
    db.create_all()


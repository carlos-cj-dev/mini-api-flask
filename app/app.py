from flask import Flask
from models import db
from routes import urls



app = Flask(__name__)
app.register_blueprint(urls)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)





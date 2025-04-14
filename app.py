from flask import Flask
from controller.main_controller import main_bp
from flask_sqlalchemy import SQLAlchemy
from config import Config


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()  # Create tables if not exist

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True,port=5001)
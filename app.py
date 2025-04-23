from flask import Flask
from controller.main_controller import main_bp
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app, origins=[os.getenv('CLIENT_URL')],supports_credentials=True)
    app.register_blueprint(main_bp)

    return app

app = create_app()

if __name__ == '__main__':
    #app.run(port=5001, debug=True)
    app.run()
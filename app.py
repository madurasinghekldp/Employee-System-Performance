from flask import Flask
from controller.main_controller import main_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
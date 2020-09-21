from flask import Flask
from dotenv import load_dotenv


def create_app(loaded_env=".env"):
    # Currently specifies location of databases
    load_dotenv(loaded_env)

    # Uses locations of databases loaded through dotenv
    from apis import api

    app = Flask(__name__, template_folder="templates")
    api.init_app(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)

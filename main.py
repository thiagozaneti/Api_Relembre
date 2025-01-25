from flask import Flask

def create_app():
    app = Flask(__name__)
    from api.routes.support.main import bp_suport
    app.register_blueprint(bp_suport)
    return app

#Gunicorn
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)




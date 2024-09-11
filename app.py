from flask import Flask
from flask import request

# import blueprints
from auth import auth

# Setting the static_folder variable to the dist directory for the react application
# will allow the python server to serve the built index.html for production.
app = Flask(__name__, static_folder="./client/dist", static_url_path="/")

app.register_blueprint(auth.AuthBlueprint)

# Serve the combiled React frontend build here
@app.route("/")
def home():
    return app.send_static_file("index.html")















# API to access data here
@app.route("/api/v1", methods=["GET", "POST", "DELETE", "PATCH"])
def api():
    error = None
    if request.method == "GET":
        return "Get all posts!"
    elif request.method == "POST":
        return "Add to all posts!"
    elif request.method == "DELETE":
        return "Delete all posts"
    elif request.method == "PATCH":
        return "Update post"

    else:
        return error

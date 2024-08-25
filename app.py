from flask import Flask
from flask import request

# Setting the static_folder variable to the dist directory for the react application
# will allow the python server to serve the built index.html for production.
app = Flask(__name__, static_folder="./client/dist", static_url_path="/")


@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/auth", methods=["GET", "POST", "DELETE", "PATCH"])
def api():
    error = None
    if request.method == "GET":
        return "Trying to authenticate!"

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

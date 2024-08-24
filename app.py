from flask import Flask

# Setting the static_folder variable to the dist directory for the react application
# will allow the python server to serve the built index.html for production. 
app = Flask(__name__, static_folder="./client/dist", static_url_path="/")

@app.route("/")
def home():
    return app.send_static_file('index.html')

@app.route("/api")
def api():
    return "<p>This is the server!</p>"
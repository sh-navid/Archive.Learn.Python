## python -m pip install flask
from flask import request
from flask import Flask
import json

## IMPORTANT:
# THIS CODE IS FULL OF BAD PRACTICES :)
# It's just to teach something

app = Flask(__name__)

users = {
    "Linda": {"password": "470591", "token": None},
    "Ahmad": {"password": "270091", "token": None},
    "Keyvan": {"password": "996000", "token": None},
    "David": {"password": "898989", "token": None},
}

## http://127.0.0.1:3000/auth
@app.route("/auth", methods=["GET", "POST"])
def auth():
    if request.method == "GET":
        return """GET Access Denied..."""
    if request.method == "POST":
        data = json.loads(request.data)
        print(data, type(data))
        if data["user"] in users.keys():
            password = users[data["user"]]["password"]
            if data["password"] == password:
                return "You have the correct username and password"
        return "Access Denied"
    return "None"


app.run(port=3000, debug=True)

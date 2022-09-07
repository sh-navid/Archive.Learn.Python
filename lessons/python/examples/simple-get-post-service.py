## python3 -m pip install flask
## python3 -m pip install urllib3

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from flask import request
from flask import Flask

app = Flask(__name__)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## بعد از اجرای این برنامه در مرورگر این آدرس
## را وارد کنید و خروجی آن را مشاهده کنید
## http://127.0.0.1:3000/
@app.route("/", methods=["GET"])
def home_page():
    return "<h1>HOME PAGE</h1>"


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## بعد از اجرای این برنامه در مرورگر این آدرس
## را وارد کنید و خروجی آن را مشاهده کنید
## http://127.0.0.1:3000/profile/david
@app.route("/profile/<name>", methods=["GET"])
def profile_page(name):
    return f"<h1>PROFILE: {name}</h1>"


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## بعد از اجرای این برنامه یک ترمینال باز کنید
## در ترمینال تایپ کنید
## python
## و دکمه اینتر را بزنید و سپس ۴ خط کد پایین را
## در آن کپی و اجرا کنید
"""
import urllib3
http = urllib3.PoolManager()
resp = http.request("POST", "http://127.0.0.1:3000/data",body="Hello World")
print(resp.data)
"""
@app.route("/data/", methods=["POST"])
def login_page():
    return f"<h1>DATA: {request.data}</h1>"


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
app.run(port=3000, debug=True)

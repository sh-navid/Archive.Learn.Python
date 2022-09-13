## python -m pip install flask

from flask import Flask

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# بعد از اجرای برنامه یک مرورگر باز کنید و تایپ کنید
# localhost:3000
# تا خروجی برنامه را مشاهده کنید
# آیا می توانید یک متن دیگر با رنگ قرمز به برنامه اضافه کنید؟
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
app = Flask(__name__)

@app.route("/")
def index():
    return """
        <html>
            <body>
                <h1 style="color:blue">My Website</h1>
                <h3>Description About My Website</h3>
                <script>alert("Javascript")</script>
            </body>
        </html>
    """


app.run(port=3000, debug=True)

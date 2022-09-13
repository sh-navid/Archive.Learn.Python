from crypt import methods
from flask import Flask

app = Flask(__name__)


d = {}

def export():
    out=""
    for k,v in d.items():
        out+=f"{k} - {v.ljust(8)}\n"
    return out


@app.route("/play/<id>/<choice>", methods=["GET"])
def play(id, choice):
    print(id, choice)
    d[id] = choice
    return export()


@app.route("/update", methods=["GET"])
def update():
    return export()


@app.route("/reset", methods=["GET"])
def reset():
    d.clear()
    return export()


app.run(host="0.0.0.0", port=4000, debug=True)

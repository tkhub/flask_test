from flask import Flask
from flask import render_template

Black_Tri_Stars = [ 'ガイア', 'オルテガ', 'マッシュ']
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("hello.html", items = Black_Tri_Stars)

from flask import render_template
from infrastructure import flaskSetup

app = flaskSetup.app

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
from flask import render_template

from infrastructure import flaskSetup
import repositories

app = flaskSetup.create_app()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
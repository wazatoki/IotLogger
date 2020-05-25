from flask_restful import Resource, Api
from flask_marshmallow import Marshmallow
from flask.templating import render_template

from infrastructure import flaskSetup


app = flaskSetup.create_app()
api = Api(app)
ma = Marshmallow(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
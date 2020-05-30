from flask_restful import Resource

class Asynchronous(Resource):
    def post(self):
        return {'hello': 'world'}
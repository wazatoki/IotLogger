from flask_restful import Resource

class Cyclic(Resource):
    def post(self):
        return {'hello': 'world'}
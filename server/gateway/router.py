from flask_restful import Api
from gateway import cyclic,asynchronous

url_prefix = "/api/"

def setup_api(app):
    api = Api(app)
    api.add_resource(cyclic.Cyclic, url_prefix + 'cyclic')
    api.add_resource(asynchronous.Asynchronous, url_prefix + 'asynchronous')
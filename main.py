from flask import Flask
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

class Test(Resource):
    def get(self):
        return {
            'message':'server is working',
            'status_code':200
        },200


api.add_resource(Test,'/')
app.run('0.0.0.0',port=5000)
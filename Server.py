from flask import Flask
from flask_restful import Api, Resource, reqparse
import datetime

app = Flask(__name__)
api = Api(app)

time = {"time": str(datetime.datetime.now())}


class Time(Resource):
    def get(self, request):
        if request == "getTime":
            return time["time"], 200
        return "User not found", 404


api.add_resource(Time, "/<string:request>")

from flask import Flask
from flask_restful import Api, Resource, reqparse
import datetime

app = Flask(__name__)
api = Api(app)


class Time(Resource):
    def get(self, request):
        if request == "getTime":
            return {"time": str(datetime.datetime.now())}, 200
        return "User not found", 404


api.add_resource(Time, "/<string:request>")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1330)

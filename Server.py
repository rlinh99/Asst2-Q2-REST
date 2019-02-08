from flask import Flask
from flask_restful import Api, Resource
import datetime

app = Flask(__name__)
api = Api(app)


class Time(Resource):
    # define get method
    # only get method is need, therefore no post, put and delete function defined.
    def get(self, request):
        # bind getTime to get method
        if request == "getTime":
            return {"time": str(datetime.datetime.now())}, 200
        return "Invalid method called", 404


# bind request url
api.add_resource(Time, "/<string:request>")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1330)

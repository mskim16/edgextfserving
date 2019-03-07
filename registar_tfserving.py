from flask import Flask
from flask import request
from flask_restful import Resource, Api
from flask_restful import reqparse
import requests
import consulate
import json
# import socket


app = Flask(__name__)
api = Api(app)

CONSUL_NAME = "edgex-tf-serving"
MS_IP = "129.254.73.137"
MS_PORT = 5000
MS_HTTPCHK = "http://"+MS_IP+":"+str(MS_PORT)+"/api/v1/ping"


def initConsulate():
    print("Register device-sensor to the localhost Consul")
    consul = consulate.Consul()
    consul.agent.service.register(name=CONSUL_NAME, address=MS_IP, port=MS_PORT, httpcheck=MS_HTTPCHK, interval="10s" )
    print(MS_HTTPCHK)

    print("Find device-sensor service by service id from the localhost Consul")
    service = consul.catalog.service(CONSUL_NAME)
    print(service)

class CreateHealth(Resource):
    def get(self):
        try:
            print("CreateHealth()\n")
            return {}
        except Exception as e:
            return {'error': str(e)}

class CreatePing(Resource):
    def get(self):
        try:
            print("CreatePing()\n")
            return {'value':'pong'}

        except Exception as e:
            return {'error':str(e)}

api.add_resource(CreateHealth, '/health')
api.add_resource(CreatePing, '/api/v1/ping')

if __name__ == '__main__':
    initConsulate()
    app.run(debug=True, host='0.0.0.0', port=int('5000'))
    # app.run(debug=True, httpHOST, httpPORT)

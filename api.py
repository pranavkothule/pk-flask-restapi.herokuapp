from flask import Flask
from flask_restx import Api, Resource
import requests
import json

app=Flask(__name__)
api=Api(app)


@api.route("/restcountries")
class restcountries(Resource):
    def get(self):
        resp = requests.get('https://restcountries.com/v3.1/region/europe')
        result=json.loads(resp.text)
        return result


@api.route("/publicapis")
class publicapis(Resource):
    def get(self):
        resp = requests.get('https://api.publicapis.org/entries')
        result=json.loads(resp.text)
        return result



if __name__ =="__main__":
    app.run()

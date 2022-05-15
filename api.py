from flask import Flask
from flask_restx import Api, Resource, fields
import requests
import json
from dal.query import insert_data, select_data

app = Flask(__name__)
api = Api(app)


model_expect = api.model('insert', {
    'name': fields.String(),
    'age': fields.Integer()
})


@api.route("/restcountries")
class restcountries(Resource):
    def get(self):
        resp = requests.get('https://restcountries.com/v3.1/region/europe')
        result = json.loads(resp.text)
        return result


@api.route("/publicapis")
class publicapis(Resource):
    def get(self):
        resp = requests.get('https://api.publicapis.org/entries')
        result = json.loads(resp.text)
        return result


@api.route("/insert_data_to_table")
class insertTo(Resource):
    @api.expect(model_expect)
    def get(self):
        data = api.payload
        result = insert_data(data)
        return result


@api.route("/select_table")
class selectTable(Resource):
    def get(self):
        result = select_data()
        return result

if __name__ == "__main__":
    app.run(debug=True)

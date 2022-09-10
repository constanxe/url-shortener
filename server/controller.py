from model import Url
from flask import jsonify, request
from settings import db

import random
import string

class UrlController():

    def create(self):
        url = request.get_json()['url']

        if (self.getData(url)):
            return self.findResponse(self.getData(url))

        converted_url = ''.join(random.choice(string.ascii_lowercase) for i in range(3)) + ''.join(random.choice(string.digits) for i in range(3))
        urlData = Url(url, converted_url)

        try:
            db.session.add(urlData)
            db.session.commit()
        except:
            return jsonify({
                "code": 500,
                "data": urlData.__repr__(),
                "message": "An error occurred."
            }), 500

        return jsonify({
            "code": 201,
            "data": urlData.__repr__()
        }), 201

    def find(self):
        url = request.get_json()['url']
        urlData = self.getData(url)

        return self.findResponse(urlData)


    def findResponse(self, urlData):
        if (urlData):
            return jsonify({
                "code": 200,
                "data": urlData.__repr__()
            })
        return jsonify({
            "code": 404,
            "message": "URL not found."
        }), 404

    def getData(self, url):
        return Url.query.filter_by(url=url).first()
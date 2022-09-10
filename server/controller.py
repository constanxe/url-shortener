from model import Url
from flask import jsonify, request
from settings import db


class UrlController():

    def create(self):
        url = request.get_json()['url']
        converted_url = 'test'
        urlData = Url(url, converted_url)

        try:
            db.session.add(urlData)
            db.session.commit()
        except:
            return jsonify({
                "code": 500,
                "data": urlData.__repr__(),
                "message": "An error occurred.",
                "status": False
            }), 500

        return jsonify({
            "code": 201,
            "data": urlData.__repr__()
        }), 201

    def find(self):
        url = request.get_json()['url']
        urlData = self.getData(url)
        if (urlData):
            return jsonify({
                "code": 200,
                "data": urlData.__repr__()
            })
        return jsonify({
            "code": 404,
            "message": "URL not found.",
            "status": False
        }), 404


    def getData(self, url):
        return Url.query.filter_by(url=url).first()
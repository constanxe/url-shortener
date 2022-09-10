from model import Url
from flask import jsonify, request
from settings import db


class UrlController():

    def create(self):
        url = request.get_json()['url']
        converted_url = 'test'
        urlData = Url(url, converted_url)

        db.session.add(urlData)
        db.session.commit()

        return jsonify(urlData.__repr__()), 200

    def find(self):
        url = request.get_json()['url']
        urlData = Url.query.filter_by(url=url).first()
        if (urlData):
            return jsonify(urlData.__repr__())
        return jsonify({"message": "URL does not exist", "status": False}), 404
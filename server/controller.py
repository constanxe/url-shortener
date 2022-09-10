from model import Url
from flask import jsonify, request
from settings import db


class UrlController():

    def create(self):
        data = request.get_json()
        urlData = Url(**data)
        db.session.add(urlData)
        db.session.commit()

        return jsonify(urlData.__repr__()), 200

    def find(self, url):
        urlData = Url.query.filter((Url.url == url)).first()
        if (urlData is not None):
            return jsonify(urlData.json())
        return jsonify({"message": "URL does not exist", "status": False}), 404
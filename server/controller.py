from model import Url
from flask import jsonify, request
from settings import db

import random
import string

class UrlController():

    def create(self):
        json = request.get_json()
        if ('url' not in json):
            return jsonify({
                "code": 400,
                "message": "Missing value for URL."
            }), 404

        url = json['url']
        # if url already exists in database, directly return the converted_url linked to it
        if (self.getData(url)):
            return self.findResponse(self.getData(url))

        # else, generate it and add to database
        urlData = self.generateUrlData(url)

        try:
            db.session.add(urlData)
            db.session.commit()
        except:
            try:    # retry at least once in case of generated same URL as any converted_url in database
                urlData = self.generateUrlData(url)

                db.session.add(urlData)
                db.session.commit()
            except:
                return jsonify({
                    "code": 500,
                    "data": urlData.__repr__(),
                    "message": "An error occurred creating the URL."
                }), 500

        return jsonify({
            "code": 201,
            "data": urlData.__repr__()
        }), 201

    def find(self):
        json = request.get_json()
        if ('url' not in json):
            return jsonify({
                "code": 400,
                "message": "Missing value for URL."
            }), 404

        url = json['url']
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

    def generateUrlData(self, url):
        converted_url = ''.join(random.choice(string.ascii_lowercase) for i in range(3)) + ''.join(random.choice(string.digits) for i in range(3))
        return Url(url, converted_url)
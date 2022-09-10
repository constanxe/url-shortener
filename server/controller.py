from model import Url
from flask import jsonify, request
from settings import db

import random
import string

class UrlController():

    def createUrlData(self):
        json = request.get_json()
        if ('url' not in json):
            return jsonify({
                "code": 400,
                "message": "Missing value for URL."
            }), 404

        url = json['url']

        # if url already exists in database, directly return the converted_url linked to it
        if (self.getUrlData(url)):
            return jsonify({
                "code": 200,
                "data": self.getUrlData(url).__repr__()
            })

        # else, generate it and add to database
        urlData = self.generateUrlData(url)

        try:
            self.addUrlDataToDatabase(urlData)
        except:
            try:    # retry at least once in case of generated same URL as any converted_url in database
                urlData = self.generateUrlData(url)
                self.addUrlDataToDatabase(urlData)
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


    def getUrlData(self, url):
        return Url.query.filter_by(url=url).first()

    def generateUrlData(self, url):
        converted_url = ''.join(random.choice(string.ascii_lowercase) for i in range(3)) + ''.join(random.choice(string.digits) for i in range(3))
        return Url(url, converted_url)

    def addUrlDataToDatabase(self, urlData):
        db.session.add(urlData)
        db.session.commit()
from model import Url
from flask import jsonify, redirect, request
from settings import db

import random
import string

class UrlController():
    def redirectToUrl(self, shortened_key):
        url_data = Url.query.filter_by(shortened_key=shortened_key).first()
        if url_data:
            return redirect(url_data.url)
        return "URL not found."

    def createUrlData(self):
        json = request.get_json()
        if ('url' not in json):
            return jsonify({
                "code": 400,
                "message": "Missing value for URL."
            }), 404

        url = json['url']

        # if url already exists in database, directly return the shortened_key linked to it
        if (self.getUrlData(url)):
            return jsonify({
                "code": 200,
                "data": self.getUrlData(url).__repr__()
            })

        # else, generate it and add to database
        url_data = self.generateUrlData(url)

        try:
            self.addUrlDataToDatabase(url_data)
        except:
            try:    # retry at least once in case of generated same URL as any shortened_key in database
                url_data = self.generateUrlData(url)
                self.addUrlDataToDatabase(url_data)
            except:
                return jsonify({
                    "code": 500,
                    "data": url_data.__repr__(),
                    "message": "An error occurred creating the URL."
                }), 500

        return jsonify({
            "code": 201,
            "data": url_data.__repr__()
        }), 201


    def getUrlData(self, url):
        return Url.query.filter_by(url=url).first()

    def generateUrlData(self, url):
        shortened_key = ''.join(random.choice(string.ascii_lowercase) for i in range(3)) + ''.join(random.choice(string.digits) for i in range(3))
        return Url(url, shortened_key)

    def addUrlDataToDatabase(self, url_data):
        db.session.add(url_data)
        db.session.commit()
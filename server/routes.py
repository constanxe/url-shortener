from flask import render_template
from settings import app
from controller import UrlController

UrlController = UrlController()

ROUTE_PREFIX_URL = '/'

@app.route(ROUTE_PREFIX_URL, methods=['POST'])
def createUrlData():
    return UrlController.createUrlData()

@app.route(ROUTE_PREFIX_URL + "<string:shortened_key>")
def findUrl(shortened_key):
    return UrlController.findUrl(shortened_key)
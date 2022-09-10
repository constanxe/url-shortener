from flask import render_template
from settings import app
from controller import UrlController

UrlController = UrlController()

ROUTE_PREFIX_URL = '/urls'

@app.route(ROUTE_PREFIX_URL, methods=['POST'])
def createUrl():
    return UrlController.create()

@app.route(ROUTE_PREFIX_URL)
def findUrl():
    return UrlController.find()
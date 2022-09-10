from flask import render_template
from settings import app
from controller import UrlController

UrlController = UrlController()

ROUTE_PREFIX_URL = '/'

@app.route(ROUTE_PREFIX_URL, methods=['POST'])
def createUrlData():
    return UrlController.createUrlData()

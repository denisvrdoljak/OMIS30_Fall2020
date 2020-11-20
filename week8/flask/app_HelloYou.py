#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 17:36:58 2020

@author: denisvrdoljak
"""

# import the Flask class from the flask module
from flask import Flask,request


# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello World"

@app.route('/enterargs')
def game():
    #arg1=None):
    arg1 = request.args.get('arg1')
    name = request.args.get('name')
    if arg1 is not None:
        returntext = "Arg 1 is: {}".format(arg1)
    elif name is not None:
        returntext = "Hello {}!".format(name)
    else:
        returntext = "NO ARGS PASSED!"
    return returntext

    #use as (assuming port 5000is used for flask app)
    # http://127.0.0.1:5000/enterargs?arg1=messageabc123
    # examples here:
    # https://stackoverflow.com/questions/24892035/python-flask-how-to-get-parameters-from-a-url



# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
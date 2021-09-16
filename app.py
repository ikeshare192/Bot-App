import numpy as np
from flask import Flask, request, make_response
import json
import pickle
from flask_cors import cross_origin 

app=flask(__name__)
model = pickle.load(open('rf.pickle', 'rb'))

@app.route('/webhook', methods=['POST'])
@cross_origin()

#function for getting and sending a response to dialogflow
def webhook():

    req = request.get_json(silent=True, force=True)

    res = processRequest(req)

    res = json.dumps(res, indent=4)

    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):
    
    result = req.get("queryResult")
   
    parameters = result.get("parameters")

    Petal_length = parameters.get("number")
    Petal_width = parameters.get("number1")
    Sepal_length = parameters.get("number2")
    Sepal_width = parameters.get("number3")
    int_features = [Petal_length, Petal_width, Sepal_length, Sepal_width]

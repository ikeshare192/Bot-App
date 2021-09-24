import numpy as np
from flask import Flask, request, make_response
import json
import pickle

app = Flask(__name__)

load_model = pickle.load(open('model', 'rb'))


@app.route('/')
def hello():
    return 'Hello World'

@app.route('/webhook', methods=['POST'])
def webhook():

    req = request.get_json(silent=True, force=True)
    
    result = req.get("queryResult")
   
    parameters = result.get("parameters")

    Petal_length = parameters.get("number")

    Petal_width = parameters.get("number1")

    Sepal_length = parameters.get("number2")

    Sepal_width = parameters.get("number3")

    int_features = [Petal_length, Petal_width, Sepal_length, Sepal_width]

    model_features = [int_features]

    intent = result.get("intent").get("displayName")

    if (intent=='IrisData'):
        prediction = load_model.predict(model_features)
        output = (prediction[0])

        if output == 0:
            flower = 'Setosa'

        if output == 1:
            flower = 'Versicolor'

        if output == 2:
            flower = 'Virginica'

        return{
            "fulfillmentText":"The Iris type is predicted to be ...{}".format(flower),
            "source":"webhook"
        }

if __name__ == "__main__":
    app.run()
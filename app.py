import numpy as np
from flask import Flask, request, make_response
import json
import pickle
from flask_cors import cross_origin 

app = Flask(__name__)
model = pickle.load(open('model', 'rb'))


@app.route('/')
def hello():
    return 'Hello World'

'''
@app.route('/webhook', methods=['POST'])
def webhook():
  return {
        "fulfillmentText": 'This is from the webhook',
        "source": 'webhook'
    }
'''

@app.route('/webhook', methods=['POST'])
#function for getting and sending a response to dialogflow
def webhook():

    req = request.get_json(silent=True, force=True)
    
    result = req.get("queryResult")
   
    parameters = result.get("parameters")

    Petal_length = parameters.get("number")
    Petal_width = parameters.get("number1")
    Sepal_length = parameters.get("number2")
    Sepal_width = parameters.get("number3")
    int_features = [Petal_length, Petal_width, Sepal_length, Sepal_width]

       return{
        "fulfillmentText": str(int_features)
    }

'''
    Petal_length = parameters.get("number")
    Petal_width = parameters.get("number1")
    Sepal_length = parameters.get("number2")
    Sepal_width = parameters.get("number3")
    int_features = [Petal_length, Petal_width, Sepal_length, Sepal_width]

    final_features = [np.array(int_features)]

    intent = result.get("inent").get("displayName")

    if (intent == 'IrisData'):
        prediction = model.predict(final_features)

        output = round(prediction[0],2)


        if(output==0):
            flower = 'Setosa'

        if(output==1):
            flower = 'Versicolor'

        if(output==2):
            flower = 'Virginica'

        fulfillmentText = "The Iris type seems to be... {} !".format(flower)

        return {
            "fulfillmentText":fulfillmentText
        }
'''

if __name__ == "__main__":
    app.run()
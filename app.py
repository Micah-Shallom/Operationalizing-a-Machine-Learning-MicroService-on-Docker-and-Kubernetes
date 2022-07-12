from flask import Flask, request, jsonify, render_template
from flask.logging import create_logger
from time import sleep
from numpy import round
import logging 

import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

def scale(payload):
    """Scales Payload"""
    
    LOG.info(f"Scaling Payload: \n{payload}")
    scaler = StandardScaler().fit(payload.astype(float))
    scaled_adhoc_predict = scaler.transform(payload.astype(float))
    return scaled_adhoc_predict

# @app.route("/")
# def home():
#     html = f"<h3>Sklearn Prediction Home</h3>"
#     return html.format(format)

@app.route('/')
@app.route('/home' , methods=['POST'])
def home():
    return render_template('form.html' , title="Home")


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/home' to submit form"

    if request.method == 'POST':
        """Performs an sklearn prediction
        
        input looks like:
        {
        "CHAS":{
        "0":0
        },
        "RM":{
        "0":6.575
        },
        "TAX":{
        "0":296.0
        },
        "PTRATIO":{
        "0":15.3
        },
        "B":{
        "0":396.9
        },
        "LSTAT":{
        "0":4.98
        }
        
        result looks like:
        { "prediction": [ <val> ] }
        
        """

        form_data = request.form
        data = []
        for key, value in dict(form_data).items():
            data.append(( key, { "0": float(value) } ))

        prep_data = dict(data)

        # # Logging the input payload
        # json_payload = request.json
        # LOG.info(f"JSON payload: \n{json_payload}")
        # inference_payload = pd.DataFrame(json_payload)

        inference_payload = pd.DataFrame(prep_data)
        LOG.info(f"Inference payload DataFrame: \n{inference_payload}")
        # scale the input
        scaled_payload = scale(inference_payload)
        # get an output prediction from the pretrained model, clf
        prediction = list(clf.predict(scaled_payload))
        # TO DO:  Log the output prediction value
        LOG.info(f"Output Prediction: {prediction}")
        preds = jsonify({'prediction': prediction})
        sleep(2)

        return render_template('prediction.html', form_data = form_data, prediction=round(prediction[0], decimals=3))
    


    



# @app.route("/predict" , methods=['GET','POST'])
# def data():
#     if request.method == 'GET':
#         return f"The URL /data is accessed directly. Try going to '/home' to submit form"
#     if request.method == 'POST':
#         form_data = request.form
#         data = []
#         for key, value in dict(form_data).items():
#             data.append((key, {"0": value}))
#         prep_data = dict(data)
#         return render_template('prediction.html', form_data = form_data)
    

if __name__ == "__main__":
    # load pretrained model as clf
    clf = joblib.load("./model_data/boston_housing_prediction.joblib")
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80

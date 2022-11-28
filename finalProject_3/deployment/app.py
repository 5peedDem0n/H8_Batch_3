import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, render_template

model = pickle.load(open('pipe_RF.pkl', 'rb'))
app = Flask(__name__, static_folder='static')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    feature = [np.array(float_features)]

    prediction = model.predict(feature)

    output = {0.0:'Lived', 1.0:'Died'}
    return render_template('index.html', prediction_text='{}'.format(output[prediction[0]]))

if __name__=='__main__':
    app.run(debug=True)
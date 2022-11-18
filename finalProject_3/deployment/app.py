import pickle
import pandas as pd
from flask import Flask, request

app = Flask(__name__)

with open('pipeline.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_data(new_data, model):
    columns = ['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes',
       'ejection_fraction', 'high_blood_pressure', 'platelets',
       'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time']
    df_data = pd.DataFrame([new_data], columns=columns)
    res = model.predict(df_data)
    return 'Lived' if res[0] == 0 else 'Died'

@app.route("/")
def halo():
    args = request.args
    age = args.get('age', type=float, default=0)
    anaemia = args.get('anaemia', type=float, default=0)
    cpk = args.get('cpk', type=float, default=0)
    diabetes = args.get('diabetes', type=float, default=0)
    ef = args.get('ef', type=float, default=0)
    hypertension = args.get('hypertension', type=float, default=0)
    platelets = args.get('platelets', type=float, default=0)
    serum_creatinine = args.get('serum_creatinine', type=float, default=0)
    serum_sodium = args.get('serum_sodium', type=float, default=0)
    sex = args.get('sex', type=float, default=0)
    smoking = args.get('smoking', type=float, default=0)
    time = args.get('time', type=float, default=0)
    new_data = [age, anaemia, cpk, diabetes, ef, 
                hypertension, platelets, serum_creatinine,
                serum_sodium, sex, smoking, time]
    res = predict_data(new_data, model)
    return {'result':res}

# app.run(debug=True)
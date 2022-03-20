#import flask
from flask import Flask, request, jsonify
import traceback
import pickle
import pandas as pd

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

# index


@app.route('/')
def home():
    return '''<h1>Ini adalah Home Page</h1>
    <p>silahkan menggunakan endpoint berikut untuk melakukan prediksi:</p>
    <ul>
        <li>/predict</li>
    </ul>'''

# predict


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            json_ = request.get_json()
            input_data = pd.DataFrame([json_])
            print(input_data)
            prediction = model.predict(input_data)
            output = {0: "Not Churn", 1: "Churn"}
            test = {'prediction': output[prediction[0]]}
            print(output)
            return jsonify({
                'status': 'success',
                'prediction': output[prediction[0]]
            })
        except:
            return jsonify({
                'status': 'fail',
                'message': traceback.format_exc()
            })


if __name__ == '__main__':
    app.run()

import sys,os
sys.path.append('.')
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from flask_cors import CORS
from Train.predict import load_model, predict_ml, get_config, process_text

app = Flask(__name__)
CORS(app)
configs = get_config()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.get_json(silent=True).get('text')
    # print(request.form)
    # text = request.form.get('text')
    print("text", text)
    if text is not None:
        lines = process_text(text)
        entity, output = predict_ml(lines=lines, pred_config=configs)
        return jsonify({"prediction": str(output[0])})
    else:
        return jsonify({'error': 'Input text not provided.'})

@app.route('/predict_web', methods=['POST'])
def predict_web():
    # text = request.get_json(silent=True).get('text')
    # print(request.form)
    text = request.form.get('text')
    # print("text", text)
    if text is not None:
        lines = process_text(text)
        entity, output = predict_ml(lines=lines, pred_config=configs)
        return jsonify({"prediction": str(output[0])})
    else:
        return jsonify({'error': 'Input text not provided.'})

if __name__ == '__main__':
    app.run(debug=True)
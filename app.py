from flask import Flask, request, render_template, jsonify
from joblib import load
import numpy as np

app = Flask(__name__)

# Load your trained model
model = load('DDOS_model01.joblib')

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        try:
            # Extract data from form, process it, and predict
            data_input = request.form['data']
            data_array = np.array([float(x) for x in data_input.split(',')]).reshape(1, -1)
            prediction = model.predict(data_array)[0]
            prediction = 'DDoS Attack Detected' if prediction == 1 else 'No DDOS Attack Detected'
        except Exception as e:
            prediction = str(e)
    return render_template('web.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
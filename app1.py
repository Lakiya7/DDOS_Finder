# ISP_Web_App/app.py
from flask import Flask, request, render_template, redirect, url_for, session, jsonify
import requests
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

GOOGLE_CLIENT_ID = "460420813801-grpprcpbs2nb823ucunraccfa08184il.apps.googleusercontent.com"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    token = data.get('token')
    user_name = data.get('user_name')

    # Verify the ID token with Google's API
    try:
        response = requests.get(
            f'https://oauth2.googleapis.com/tokeninfo?id_token={token}'
        )
        response.raise_for_status()
        user_info = response.json()

        if user_info['aud'] != GOOGLE_CLIENT_ID:
            return jsonify({'message': 'Invalid Google client ID'}), 401

        # Save user session
        session['user_name'] = user_name
        return jsonify({'message': 'User authenticated'}), 200

    except requests.exceptions.RequestException as e:
        print(f'Error verifying ID token: {e}')
        return jsonify({'message': 'Error verifying ID token'}), 401

@app.route('/welcome')
def welcome():
    user_name = session.get('user_name')
    if not user_name:
        return redirect(url_for('index'))
    return render_template('web.html', user_name=user_name)

if __name__ == '__main__':
    app.run(debug=True)

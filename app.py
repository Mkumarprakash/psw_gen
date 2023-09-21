# app.py
import random
import string
from flask import Flask, request, jsonify

app = Flask(__name__)

def Gen_password(length=8):
    characters = string.digits + string.ascii_letters  # + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/generate-password', methods=['GET'])
def generate_password():
    length = int(request.args.get('length', 8))
    password = Gen_password(length)
    return jsonify({"password": password})

if __name__ == '__main__':
    app.run(debug=True)

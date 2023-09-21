from flask import Flask, render_template
from generator import Gen_password

app = Flask(__name__)

@app.route('/')
def index():
    password = Gen_password()
    return render_template('index.html', password=password)


if __name__ == '__main__':
    app.run(debug=True)

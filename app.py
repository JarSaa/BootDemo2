from flask import Flask, render_template
from db.data import get_taxes
from api import generate_json

app = Flask(__name__)

@app.route('/api/all')
def api_app():
    return generate_json(get_taxes())

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from flask import request
import requests

app = Flask(__name__)

@app.route('/')
def index():
   return render_template(‘index.html’)

@app.route('/l2')
def index():
   return render_template(‘l2.html’)

@app.route('/l3')
def index():
   return render_template(‘l3.html’)

@app.route('/l4')
def index():
   return render_template(‘l4.html’)

@app.route('/api')
def api():
    r


if __name__ == '__main__':
   app.run(debug = True)
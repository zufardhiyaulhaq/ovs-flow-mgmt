from flask import Flask, render_template
from flask import request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/l2')
def l2():
   return render_template('l2.html')

@app.route('/l3')
def l3():
   return render_template('l3.html')

@app.route('/l4')
def l4():
   return render_template('l4.html')

@app.route('/api', methods = ['POST'])
def api():
    data = request.get_json()

if __name__ == '__main__':
   app.run(debug = True)
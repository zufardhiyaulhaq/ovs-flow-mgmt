from flask import Flask, render_template
from flask import request
import requests
import json

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


@app.route('/api', methods=['POST'])
def api():
    data = request.form.to_dict(flat=True)

    url = str("http://"+str(data['device_ip'])+":"+str(data['port'])+"/api")
    username = str(data['username'])
    password = str(data['password'])

    del data['device_ip']
    del data['username']
    del data['password']
    del data['port']

    flowmod = {
        "layer": None,
        "src_mac": None,
        "dst_mac": None,
        "src_ip": None,
        "dst_ip": None,
        "protocol": None,
        "src_port": None,
        "dst_port": None,
        "action": None,
        "bridge": None
    }
    
    for key, value in data.items():
        if value == "":
            data.pop(key)

    flowmod.update(data)
    data = json.dumps(flowmod)

    post = requests.post(url=url,  auth=(username, password), data=data, headers={"content-type":"application/json"})
    return "added"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)

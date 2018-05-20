from flask import Flask, render_template
from flask_basicauth import BasicAuth
from flask import request

import os

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'john'
app.config['BASIC_AUTH_PASSWORD'] = 'matrix'
app.config['BASIC_AUTH_FORCE'] = True

@app.route('/api', methods = ['POST'])
def postJsonHandler():
    data = request.get_json()
    if data['layer']=='l2':
        l2Handler(data)
        return "l2 flow is added"
    else if data['layer']=='l3':
        l3Handler(data)
        return "l3 flow is added"
    else if data['layer']=='l4':
        l4Handler(data)
        return "l4 flow is added"
    else:
        return "not spesific the layer!"

def l2Handler(data):
    if data['src_mac']!=NULL:
        src_mac = data['src_mac']
    
    if data['dst_mac']!=NULL:
        dst_mac = data['dst_mac']

    if data['action']!=NULL:
        action = data['action']

    if data['bridge']!=NULL:
        bridge = data['bridge']

    if ((data['src_mac']!=NULL) and (data['dst_mac']==NULL)) and ((data['action']!=NULL) and (data['bridge']!=NULL)):
        command = 'ovs-ofctl add-flow %s dl_src=%s,actions=%s' %(bridge,src_mac,action)
    
    if ((data['src_mac']==NULL) and (data['dst_mac']!=NULL)) and ((data['action']!=NULL) and (data['bridge']!=NULL)):
        command = 'ovs-ofctl add-flow %s dl_dst=%s,actions=%s' %(bridge,dst_mac,action)
    
    if ((data['src_mac']!=NULL) and (data['dst_mac']!=NULL)) and ((data['action']!=NULL) and (data['bridge']!=NULL)):
        command = 'ovs-ofctl add-flow %s dl_src=%s,dl_dst=%s,actions=%s' %(bridge,src_mac,dst_mac,action)
        
    os.system(command)

# {
#     'layer':['l2','l3','l4'],
#     'src_mac':[],
#     'dst_mac':[], 
#     'src_ip':[],
#     'dst_ip':[],
#     'protocol':['tcp','udp'],
#     'src_port':[]
#     'dst_port':[]
#     'action':['drop']
#     'bridge':['']
# }
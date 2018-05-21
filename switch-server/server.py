from flask import Flask, render_template
from flask_basicauth import BasicAuth
from flask import request

import os

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'john'
app.config['BASIC_AUTH_PASSWORD'] = 'matrix'
app.config['BASIC_AUTH_FORCE'] = True

@app.route('/api', methods = ['POST'])
@login_required
def postJsonHandler():
    data = request.get_json()
    print (data)
    if data['layer']=='l2':
        l2Handler(data)
        return "l2 flow is added"
    elif data['layer']=='l3':
        l3Handler(data)
        return "l3 flow is added"
    elif data['layer']=='l4':
        l4Handler(data)
        return "l4 flow is added"
    else:
        return "not spesific the layer!"

def l2Handler(data):
    action = data['action']
    bridge = data['bridge']

    if (data['src_mac']!=None) and (data['dst_mac']==None):
        src_mac = data['src_mac']
        command = 'sudo ovs-ofctl add-flow %s dl_src=%s,actions=%s' %(bridge,src_mac,action)
    
    elif (data['src_mac']==None) and (data['dst_mac']!=None):
        dst_mac = data['dst_mac']
        command = 'sudo ovs-ofctl add-flow %s dl_dst=%s,actions=%s' %(bridge,dst_mac,action)
    
    elif (data['src_mac']!=None) and (data['dst_mac']!=None):
        src_mac = data['src_mac']
        dst_mac = data['dst_mac']
        command = 'sudo ovs-ofctl add-flow %s dl_src=%s,dl_dst=%s,actions=%s' %(bridge,src_mac,dst_mac,action)

    os.system(command)

def l3Handler(data):
    action = data['action']
    bridge = data['bridge']

    if ((data['src_mac']==None) and (data['dst_mac']==None)):
 
        if (data['src_ip']!=None) and (data['dst_ip']==None):
            src_ip = data['src_ip']
            command = 'sudo ovs-ofctl add-flow %s ip,nw_src=%s,actions=%s' %(bridge,src_ip,action)
        
        elif (data['src_ip']==None) and (data['dst_ip']!=None):
            dst_ip = data['dst_ip']
            command = 'sudo ovs-ofctl add-flow %s ip,nw_dst=%s,actions=%s' %(bridge,dst_ip,action)
        
        elif (data['src_ip']!=None) and (data['dst_ip']!=None):
            src_ip = data['src_ip']
            dst_ip = data['dst_ip']
            command = 'sudo ovs-ofctl add-flow %s ip,nw_src=%s,nw_dst=%s,actions=%s' %(bridge,src_ip,dst_ip,action)
    
    elif ((data['src_mac']!=None) and (data['dst_mac']==None)):
        src_mac = data['src_mac']
        
        if (data['src_ip']!=None) and (data['dst_ip']==None):
            src_ip = data['src_ip']
            command = 'sudo ovs-ofctl add-flow %s ip,dl_src=%s,nw_src=%s,actions=%s' %(bridge,src_mac,src_ip,action)
        
        elif (data['src_ip']==None) and (data['dst_ip']!=None):
            dst_ip = data['dst_ip']
            command = 'sudo ovs-ofctl add-flow %s ip,dl_src=%s,nw_dst=%s,actions=%s' %(bridge,src_mac,dst_ip,action)
        
        elif (data['src_ip']!=None) and (data['dst_ip']!=None):
            src_ip = data['src_ip']
            dst_ip = data['dst_ip']
            command = 'sudo ovs-ofctl add-flow %s ip,dl_src=%s,nw_src=%s,nw_dst=%s,actions=%s' %(bridge,src_mac,src_ip,dst_ip,action)
    
    elif ((data['src_mac']==None) and (data['dst_mac']!=None)):
        dst_mac = data['dst_mac']
        
        if (data['src_ip']!=None) and (data['dst_ip']==None):
            src_ip = data['src_ip']
            command = 'sudo ovs-ofctl add-flow %s ip,dl_dst=%s,nw_src=%s,actions=%s' %(bridge,dst_mac,src_ip,action)
        
        elif (data['src_ip']==None) and (data['dst_ip']!=None):
            dst_ip = data['dst_ip']
            command = 'sudo ovs-ofctl add-flow %s ip,dl_dst=%s,nw_dst=%s,actions=%s' %(bridge,dst_mac,dst_ip,action)
        
        elif (data['src_ip']!=None) and (data['dst_ip']!=None):
            src_ip = data['src_ip']
            dst_ip = data['dst_ip']
            command = 'sudo ovs-ofctl add-flow %s ip,dl_dst=%s,nw_src=%s,nw_dst=%s,actions=%s' %(bridge,dst_mac,src_ip,dst_ip,action)
    
    elif ((data['src_mac']!=None) and (data['dst_mac']!=None)):
        src_mac = data['src_mac']
        dst_mac = data['dst_mac']
        
        if (data['src_ip']!=None) and (data['dst_ip']==None):
            src_ip = data['src_ip']
            command = 'sudo ovs-ofctl add-flow %s ip,dl_src=%s,dl_dst=%s,nw_src=%s,actions=%s' %(bridge,src_mac,dst_mac,src_ip,action)
        
        elif (data['src_ip']==None) and (data['dst_ip']!=None):
            dst_ip = data['dst_ip']
            command = 'sudo ovs-ofctl add-flow %s ip,dl_src=%s,dl_dst=%s,nw_dst=%s,actions=%s' %(bridge,src_mac,dst_mac,dst_ip,action)
        
        elif (data['src_ip']!=None) and (data['dst_ip']!=None):
            src_ip = data['src_ip']
            dst_ip = data['dst_ip']
            command = 'sudo ovs-ofctl add-flow %s ip,dl_src=%s,dl_dst=%s,nw_src=%s,nw_dst=%s,actions=%s' %(bridge,src_mac,dst_mac,src_ip,dst_ip,action)

    os.system(command)

def l4Handler(data):
    action = data['action']
    bridge = data['bridge']
    protocol = data['protocol']

    if ((data['src_port']!=None) and (data['dst_port']==None)):
        src_port = data['src_port']

        if ((data['src_mac']==None) and (data['dst_mac']==None)):

            if (data['src_ip']!=None) and (data['dst_ip']==None):
                src_ip = data['src_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,nw_src=%s,tp_src=%s,actions=%s' %(bridge,protocol,src_ip,src_port,action)
            
            elif (data['src_ip']==None) and (data['dst_ip']!=None):
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,nw_dst=%s,tp_src=%s,actions=%s' %(bridge,protocol,dst_ip,src_port,action)
            
            elif (data['src_ip']!=None) and (data['dst_ip']!=None):
                src_ip = data['src_ip']
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,nw_src=%s,nw_dst=%s,tp_src=%s,actions=%s' %(bridge,protocol,src_ip,dst_ip,src_port,action)
        
        elif ((data['src_mac']!=None) and (data['dst_mac']==None)):
            src_mac = data['src_mac']
            
            if (data['src_ip']!=None) and (data['dst_ip']==None):
                src_ip = data['src_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_src=%s,nw_src=%s,tp_src=%s,actions=%s' %(bridge,protocol,src_mac,src_ip,src_port,action)
            
            elif (data['src_ip']==None) and (data['dst_ip']!=None):
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_src=%s,nw_dst=%s,tp_src=%s,actions=%s' %(bridge,protocol,src_mac,dst_ip,src_port,action)
            
            elif (data['src_ip']!=None) and (data['dst_ip']!=None):
                src_ip = data['src_ip']
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_src=%s,nw_src=%s,nw_dst=%s,tp_src=%s,actions=%s' %(bridge,protocol,src_mac,src_ip,dst_ip,src_port,action)
        
        elif ((data['src_mac']==None) and (data['dst_mac']!=None)):
            dst_mac = data['dst_mac']
            
            if (data['src_ip']!=None) and (data['dst_ip']==None):
                src_ip = data['src_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_dst=%s,nw_src=%s,tp_src=%s,actions=%s' %(bridge,protocol,dst_mac,src_ip,src_port,action)
            
            elif (data['src_ip']==None) and (data['dst_ip']!=None):
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_dst=%s,nw_dst=%s,tp_src=%s,actions=%s' %(bridge,protocol,dst_mac,dst_ip,src_port,action)
            
            elif (data['src_ip']!=None) and (data['dst_ip']!=None):
                src_ip = data['src_ip']
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_dst=%s,nw_src=%s,nw_dst=%s,tp_src=%s,actions=%s' %(bridge,protocol,dst_mac,src_ip,dst_ip,src_port,action)
        
        elif ((data['src_mac']!=None) and (data['dst_mac']!=None)):
            src_mac = data['src_mac']
            dst_mac = data['dst_mac']
            
            if (data['src_ip']!=None) and (data['dst_ip']==None):
                src_ip = data['src_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_src=%s,dl_dst=%s,nw_src=%s,tp_src=%s,actions=%s' %(bridge,protocol,src_mac,dst_mac,src_ip,src_port,action)
            
            elif (data['src_ip']==None) and (data['dst_ip']!=None):
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_src=%s,dl_dst=%s,nw_dst=%s,tp_src=%s,actions=%s' %(bridge,protocol,src_mac,dst_mac,dst_ip,src_port,action)
            
            elif (data['src_ip']!=None) and (data['dst_ip']!=None):
                src_ip = data['src_ip']
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_src=%s,dl_dst=%s,nw_src=%s,nw_dst=%s,tp_src=%s,actions=%s' %(bridge,protocol,src_mac,dst_mac,src_ip,dst_ip,src_port,action)
    
    elif ((data['src_port']==None) and (data['dst_port']!=None)):
        dst_port = data['dst_port']

        if ((data['src_mac']==None) and (data['dst_mac']==None)):

            if (data['src_ip']!=None) and (data['dst_ip']==None):
                src_ip = data['src_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,nw_src=%s,tp_dst=%s,actions=%s' %(bridge,protocol,src_ip,dst_port,action)
            
            elif (data['src_ip']==None) and (data['dst_ip']!=None):
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,nw_dst=%s,tp_dst=%s,actions=%s' %(bridge,protocol,dst_ip,dst_port,action)
            
            elif (data['src_ip']!=None) and (data['dst_ip']!=None):
                src_ip = data['src_ip']
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,nw_src=%s,nw_dst=%s,tp_dst=%s,actions=%s' %(bridge,protocol,src_ip,dst_ip,dst_port,action)
        
        elif ((data['src_mac']!=None) and (data['dst_mac']==None)):
            src_mac = data['src_mac']
            
            if (data['src_ip']!=None) and (data['dst_ip']==None):
                src_ip = data['src_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_src=%s,nw_src=%s,tp_dst=%s,actions=%s' %(bridge,protocol,src_mac,src_ip,dst_port,action)
            
            elif (data['src_ip']==None) and (data['dst_ip']!=None):
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_src=%s,nw_dst=%s,tp_dst=%s,actions=%s' %(bridge,protocol,src_mac,dst_ip,dst_port,action)
            
            elif (data['src_ip']!=None) and (data['dst_ip']!=None):
                src_ip = data['src_ip']
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_src=%s,nw_src=%s,nw_dst=%s,tp_dst=%s,actions=%s' %(bridge,protocol,src_mac,src_ip,dst_ip,dst_port,action)
        
        elif ((data['src_mac']==None) and (data['dst_mac']!=None)):
            dst_mac = data['dst_mac']
            
            if (data['src_ip']!=None) and (data['dst_ip']==None):
                src_ip = data['src_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_dst=%s,nw_src=%s,tp_dst=%s,actions=%s' %(bridge,protocol,dst_mac,src_ip,dst_port,action)
            
            elif (data['src_ip']==None) and (data['dst_ip']!=None):
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_dst=%s,nw_dst=%s,tp_dst=%s,actions=%s' %(bridge,protocol,dst_mac,dst_ip,dst_port,action)
            
            elif (data['src_ip']!=None) and (data['dst_ip']!=None):
                src_ip = data['src_ip']
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_dst=%s,nw_src=%s,nw_dst=%s,tp_dst=%s,actions=%s' %(bridge,protocol,dst_mac,src_ip,dst_ip,dst_port,action)
        
        elif ((data['src_mac']!=None) and (data['dst_mac']!=None)):
            src_mac = data['src_mac']
            dst_mac = data['dst_mac']
            
            if (data['src_ip']!=None) and (data['dst_ip']==None):
                src_ip = data['src_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_src=%s,dl_dst=%s,nw_src=%s,tp_dst=%s,actions=%s' %(bridge,protocol,src_mac,dst_mac,src_ip,dst_port,action)
            
            elif (data['src_ip']==None) and (data['dst_ip']!=None):
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_src=%s,dl_dst=%s,nw_dst=%s,tp_dst=%s,actions=%s' %(bridge,protocol,src_mac,dst_mac,dst_ip,dst_port,action)
            
            elif (data['src_ip']!=None) and (data['dst_ip']!=None):
                src_ip = data['src_ip']
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_src=%s,dl_dst=%s,nw_src=%s,nw_dst=%s,tp_dst=%s,actions=%s' %(bridge,protocol,src_mac,dst_mac,src_ip,dst_ip,dst_port,action)

    elif ((data['src_port']!=None) and (data['dst_port']!=None)):
        src_port = data['src_port']
        dst_port = data['dst_port']

        if ((data['src_mac']==None) and (data['dst_mac']==None)):

            if (data['src_ip']!=None) and (data['dst_ip']==None):
                src_ip = data['src_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,nw_src=%s,tp_src=%s,tp_dst=%s,actions=%s' %(bridge,protocol,src_ip,src_port,dst_port,action)
            
            elif (data['src_ip']==None) and (data['dst_ip']!=None):
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,nw_dst=%s,tp_src=%s,tp_dst=%s,actions=%s' %(bridge,protocol,dst_ip,src_port,dst_port,action)
            
            elif (data['src_ip']!=None) and (data['dst_ip']!=None):
                src_ip = data['src_ip']
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,nw_src=%s,nw_dst=%s,tp_src=%s,tp_dst=%s,actions=%s' %(bridge,protocol,src_ip,dst_ip,src_port,dst_port,action)
        
        elif ((data['src_mac']!=None) and (data['dst_mac']==None)):
            src_mac = data['src_mac']
            
            if (data['src_ip']!=None) and (data['dst_ip']==None):
                src_ip = data['src_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_src=%s,nw_src=%s,tp_src=%s,tp_dst=%s,actions=%s' %(bridge,protocol,src_mac,src_ip,src_port,dst_port,action)
            
            elif (data['src_ip']==None) and (data['dst_ip']!=None):
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_src=%s,nw_dst=%s,tp_src=%s,tp_dst=%s,actions=%s' %(bridge,protocol,src_mac,dst_ip,src_port,dst_port,action)
            
            elif (data['src_ip']!=None) and (data['dst_ip']!=None):
                src_ip = data['src_ip']
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_src=%s,nw_src=%s,nw_dst=%s,tp_src=%s,tp_dst=%s,actions=%s' %(bridge,protocol,src_mac,src_ip,dst_ip,src_port,dst_port,action)
        
        elif ((data['src_mac']==None) and (data['dst_mac']!=None)):
            dst_mac = data['dst_mac']
            
            if (data['src_ip']!=None) and (data['dst_ip']==None):
                src_ip = data['src_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_dst=%s,nw_src=%s,tp_src=%s,tp_dst=%s,actions=%s' %(bridge,protocol,dst_mac,src_ip,src_port,dst_port,action)
            
            elif (data['src_ip']==None) and (data['dst_ip']!=None):
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_dst=%s,nw_dst=%s,tp_src=%s,tp_dst=%s,actions=%s' %(bridge,protocol,dst_mac,dst_ip,src_port,dst_port,action)
            
            elif (data['src_ip']!=None) and (data['dst_ip']!=None):
                src_ip = data['src_ip']
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_dst=%s,nw_src=%s,nw_dst=%s,tp_src=%s,tp_dst=%s,actions=%s' %(bridge,protocol,dst_mac,src_ip,dst_ip,src_port,dst_port,action)
        
        elif ((data['src_mac']!=None) and (data['dst_mac']!=None)):
            src_mac = data['src_mac']
            dst_mac = data['dst_mac']
            
            if (data['src_ip']!=None) and (data['dst_ip']==None):
                src_ip = data['src_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_src=%s,dl_dst=%s,nw_src=%s,tp_src=%s,tp_dst=%s,actions=%s' %(bridge,protocol,src_mac,dst_mac,src_ip,src_port,dst_port,action)
            
            elif (data['src_ip']==None) and (data['dst_ip']!=None):
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_src=%s,dl_dst=%s,nw_dst=%s,tp_src=%s,tp_dst=%s,actions=%s' %(bridge,protocol,src_mac,dst_mac,dst_ip,src_port,dst_port,action)
            
            elif (data['src_ip']!=None) and (data['dst_ip']!=None):
                src_ip = data['src_ip']
                dst_ip = data['dst_ip']
                command = 'sudo ovs-ofctl add-flow %s %s,dl_src=%s,dl_dst=%s,nw_src=%s,nw_dst=%s,tp_src=%s,tp_dst=%s,actions=%s' %(bridge,protocol,src_mac,dst_mac,src_ip,dst_ip,src_port,dst_port,action)
    
    os.system(command)

if __name__ == '__main__':
   app.run(host="0.0.0.0",port=5000,debug=True)
# ovs-flow-mgmt
OpenVSwitch OpenFlow Flow Management is a Web Based Flow Management for OpenVSwitch. This project is help network engineer deploy rule to OpenVSwitch via dashboard.

### Feature
1. L2/L3/L4 Flow matching & Modifier
1. Web Dashboard Controller

### Parameter Flow Matching
- Source/Destination MAC Address 
- Source/Destination IP Address
- TCP/UDP Support & Source/Destination Port

### Concept
![alt text](https://raw.githubusercontent.com/zufardhiyaulhaq/ovs-flow-mgmt/master/images/concept.png)

### Custom Web Dashboard
We have hard work to create dashboard for controlling the devices. but if you want to create your own dashboard or want to integrate this system, you can follow this step.
- switch-server is API for translating json flow to flow table in the devices, create dashboard that can send this following json.
```
{
    "layer":"l4",
    "src_mac":null,
    "dst_mac":null, 
    "src_ip":null,
    "dst_ip":"172.1.31.1",
    "protocol":"udp",
    "src_port":null,
    "dst_port":"53",
    "action":"drop",
    "bridge":"br1"
}
```
this is the example of sending layer 4 rule to the devices.
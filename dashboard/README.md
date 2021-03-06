Dashboard API
=============

Simple Dashboard to deploy rule into OpenVSwitch

### Deployment
- clone the repository
```
git clone https://github.com/zufardhiyaulhaq/ovs-flow-mgmt
```
- Copy service for the API and copy dashboard directory.
```
cd ovs-flow-mgmt
sudo cp script/dashboard.service /etc/systemd/system/
mkdir /var/www/html/
sudo cp -R dashboard/ /var/www/html/
sudo chown user:user -R /var/www/html/dashboard/
```
- Install Python virtualenv and requirements.
```
cd /var/www/html/dashboard/
sudo virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
- Running the API
```
sudo systemctl start dashboard
```
- Open The Dashboard
```
http://<ip-address>:4000/
```

### Screenshot
![alt text](https://raw.githubusercontent.com/zufardhiyaulhaq/ovs-flow-mgmt/master/images/screenshot2.png)
![alt text](https://raw.githubusercontent.com/zufardhiyaulhaq/ovs-flow-mgmt/master/images/screenshot.png)

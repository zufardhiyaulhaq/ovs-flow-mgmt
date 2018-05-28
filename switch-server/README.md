switch-server API
=================

A simple API server in the device node to receive and automaticaly deploy the command from the dashboard.

### Deployment
- clone the repository
```
git clone https://github.com/zufardhiyaulhaq/ovs-flow-mgmt
```
- Copy service for the API and copy switch-server directory.
```
cd ovs-flow-mgmt
sudo cp script/switch-server.service /etc/systemd/system/
mkdir /var/www/html/
sudo cp -R switch-server/ /var/www/html/
sudo chown user:user -R /var/www/html/switch-server/
```
- Install Python virtualenv and requirements.
```
cd /var/www/html/switch-server/
sudo virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
- Change the API username & password
```
nano server.py
```
- Running the API
```
sudo systemctl start switch-server
```

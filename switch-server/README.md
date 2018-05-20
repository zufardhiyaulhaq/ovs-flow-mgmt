switch-server API
=================

A simple API server in the device node to receive and automaticaly deploy the command from the dashboard.

### Deployment
```
git clone https://github.com/zufardhiyaulhaq/ovs-flow-mgmt
```
clone the repository

```
cd ovs-flow-mgmt
sudo cp scripts/switch-server.service /etc/systemd/system/
mkdir /var/www/html/
cp -R switch-server/ /var/www/html/
```
Copy service for the API and copy switch-server directory.

```
cd /var/www/html/switch-server/
virtualenv
source/env/bin/activate
pip install -r requirements.txt
```
Install Python virtualenv and requirements.

```
nano server.py
````
change the API username & password

```
sudo systemctl start switch-server
```
Running the API

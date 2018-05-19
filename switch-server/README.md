git clone https://github.com/zufardhiyaulhaq/ovs-flow-mgmt

sudo cp scripts/switch-server.service /etc/systemd/system/
cd ovs-flow-mgmt
cp -R switch-server /var/www/html/

/var/www/html/switch-server/
virtualenv
source/env/bin/activate
pip install -r requirements.txt

sudo systemctl start switch-server


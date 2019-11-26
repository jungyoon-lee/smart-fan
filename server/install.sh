sudo apt install python3 python3-pip

export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo apt install virtualenv
virtualenv venv -p python3
source ./venv/bin/activate
pip install -r require.txt

sudo apt install libmysqlclient-dev build-essential libssl-dev libffi-dev
sudo apt install mysql-server

sudo apt install nodejs npm
ln -s /usr/bin/nodejs /usr/local/bin/node
sudo npm install -g bower
bower install

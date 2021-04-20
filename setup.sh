#!/bin/bash

sudo pip install virtualenv virtualenvwrapper
sudo rm -rf ~/get-pip.py ~/.cache/pip

# Update and reload .bashrc
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
source ~/.bashrc

# Create virtual environment
mkvirtualenv cv -p python3

# Install additional modules
workon cv
pip install gunicorn
#pip install -r requirements.txt
python -c "import cv2; print(cv2.__version__)"

sudo cp server.conf /etc/supervisor/conf.d/f-barnacle-server.conf
sudo mkdir -p /var/log/f-barnacle-server/
sudo touch /var/log/f-barnacle-server/fbs-err.log
sudo touch /var/log/f-barnacle-server/fbs-out.log
sudo supervisorctl reload
chmod +x serve.sh

sudo apt-get install gunicorn nginx -y
sudo rm /etc/ngix/sites-enabled/default
sudo cp f-bs-nginx /etc/ngix/sites-enabled/f-bs-nginx

sudo apt-get install ufw -y
sudo ufw default allow outgoing
sudo ufw default deny incoming
sudo ufw allow ssh
sudo ufw allow http/tcp
sudo ufw allow 80
sudo ufw allow 443
sudo ufw allow 8080
sudo ufw status
#
sudo ufw enable -y
sudo systemctl restart nginx -y
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
#pip install -r requirements.txt
python -c "import cv2; print(cv2.__version__)"

cp server.conf /etc/supervisor/conf.d/f-barnacle-server.conf
sudo mkdir -p /var/log/f-barnacle-server/
sudo touch var/log/f-barnacle-server/fbs-err.log
sudo touch var/log/f-barnacle-server/fbs-out.log
sudo supervisorctl reload
chmod +x serve.sh
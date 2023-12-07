#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx

#creating folders if not already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

#creating sample html file for  testing
sudo touch /data/web_static/releases/test/index.html
echo "Hello there, I'm Cyril!" | sudo tee /data/web_static/releases/test/index.html > /dev/null

#creating a symbol link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#assigning ownership of /data/ to ubuntu
chown -R ubuntu:ubuntu /data/

#editing the nginx config file
str="\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\tindex index.html 0-index.html 0-index.htm;\n\t}"
sudo sed -i "/^\tserver_name .*;/a ${str}" /etc/nginx/sites-enabled/default

# restart nginx
sudo service nginx restart

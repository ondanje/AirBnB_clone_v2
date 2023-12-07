#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx

#creating folders if not already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

#creating sample html file
sudo touch /data/web_static/releases/test/index.html
echo "Hello there, I'm Cyril!" | sudo tee /data/web_static/releases/test/index.html > /dev/null

#creating a symbol link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#assigning ownership of /data/ to ubuntu
chown -R ubuntu:ubuntu /data/

#editing the nginx config file
config_nginx="/etc/nginx/sites-available/default/"
sudo sed -i '/hbnb_static/ {N; s/location \/ {/location \/hbnb_static\/ {alias \/data\/web_static\/current\/;}/ } }' "$config_nginx"

#restart nginx
sudo service nginx restart

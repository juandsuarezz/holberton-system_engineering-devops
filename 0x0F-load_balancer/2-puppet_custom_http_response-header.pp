#!/usr/bin/env bash
#Install nginx web server

exec { 'Install Nginx web server':
  provider => shell,
  command  => 'apt-get -y update ; apt-get -y install nginx ; echo "Holberton School" > /var/www/html/index.html ;  sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me http:\/\/suaro.co permanent;\n\tadd_header X-Served-By \$hostname;/" /etc/nginx/sites-available/default ; service nginx start'

}
#! /bin/bash

http_port=$1
https_port=$2
server_name=$3
root_path=$4

template="$(cat ./nginx/site-template.conf)";
eval "echo \"${template}\" > ./nginx/sites/default.conf" &&
docker-compose restart nginx

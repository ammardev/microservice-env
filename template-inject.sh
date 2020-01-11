#! /bin/bash

service_folder_name=$1
service_url_path=$2
template="$(cat ./nginx/service-template.conf)";
eval "echo \"${template}\" >> ./nginx/services/\"${service_folder_name}\".conf" &&
docker-compose restart nginx

#!/bin/bash

echo -n "Insert service folder name: ";
read ans;
service_folder_name=${ans};
echo -n "Insert service path name: ";
read ans;
service_url_path=${ans}
template="$(cat ./nginx/service-template.conf)";

GREEN='\033[0;32m'
eval "echo \"${template}\" >> ./nginx/services/\"${service_folder_name}\".conf" &&
 echo -e "\n${GREEN}Service created! You need to restart nginx."

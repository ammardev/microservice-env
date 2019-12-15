#!/bin/bash

echo "This command will create a new microservice"
echo -e "and link it to an Nginx container on a subdomain\n"

echo -n "Insert service folder name: ";
read ans;
service_folder_name=${ans};

echo -e "\nStart installing new lumen service...\n";
project_dir=../src/${service_folder_name}
git clone https://github.com/3bdullahg97/lumen-mongodb.git ${project_dir};

mv ${project_dir}/.env.example ${project_dir}/.env;
docker-compose exec php bash -c "cd ${service_folder_name} && composer install && php artisan key:generate"

echo -en "\nInsert service path name: ";
read ans;
service_url_path=${ans}

template="$(cat ./nginx/service-template.conf)";

GREEN='\033[0;32m'
eval "echo \"${template}\" >> ./nginx/services/\"${service_folder_name}\".conf" &&
 echo -e "\n${GREEN}Service created! You need to restart nginx."

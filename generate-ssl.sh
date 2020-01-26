#! /bin/bash

docker-compose exec nginx bash -c "certbot --nginx --redirect --non-interactive --agree-tos -m $2 -d $1" &&
docker-compose exec nginx bash -c "echo \"0 0 * * 0 certbot renew\" >> /etc/crontabs/root" &&
docker-compose restart nginx


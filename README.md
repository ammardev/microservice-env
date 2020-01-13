# Docker Compose Setup For Microservices.
This repository is a docker-compose setup for development environement with an automated way to add new services to the system.

# Installation
To install and use this repository in your project. You should have the following directory structure:
```
/
- /docker
- /src
    - /microservice1
    - /microservice2
```

in the root folder clone the repository using the following command:
```
git clone https://github.com/ammardev/microservice-env.git docker
```

# Basic Usage
This project is a normal Docker Compose project. So you can use any `docker-compose` command. These are some important commands:

Run the containers:
```
docker-compose up
```

Stop the containers:

```
docker-compose stop
```

For more information about `docker-compose` usage checkout the [reference](https://docs.docker.com/compose/reference/).
Or you can read [these articles to learn about Docker (Arabic)](https://3alam.pro/3mmarg97/series/introduction-to-docker/)

# Creating New Services
This is a command that create new microservices in the project. The new microservice folder will be placed in `src` directory. Make sure that the directory is created with the right permissions so that the script can create project without any problems.

This command will do the following things:
* Creates a new lumen project [from this boilerplate](https://github.com/3bdullahg97/lumen-mongodb).
* Running `composer install` from inside `php` container.
* Creates an Nginx configuration so that the new service can work with Nginx.
* It will restart Nginx container automatically. So you don't have to do it by yourself.

```
python make-service.py -b folder path
```

Make service command takes two arguments. The first is the folder name in the src directory.
And the second is the path that will be used in the Nginx configuration file.
If you don't use `-b` flag, boilerplate won't be created. And the script will assume that the folder exists in src directory.

# Generate SSL certificate
After running containers. You can use `generate-ssl` command which is used to generate a new SSL certificate. The command will also
add the renew command to the cronjob and restart Nginx container.
```
./generate-ssl example.com webmaster@example.com
```

Note that the domain used in the previous command should be same as server_name in default.conf.

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
You can define your new services in nginx without editing nginx configuration files. simply run `make-service.sh` bash script:
```
./make-service.sh
```
Then you will have to choose the microservice folder name in the `src` directory. And the path that the servece will serve on it as shown in the image:

![image](https://user-images.githubusercontent.com/16087389/70798497-c502d180-1daf-11ea-809f-7e559403328f.png)


Then you should restart nginx container using the following command:
```
docker-compose restart nginx
```

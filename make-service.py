import argparse
import subprocess
import os

def newLumenProject(folder_name):
    subprocess.run(['git', 'clone', 'https://github.com/3bdullahg97/lumen-mongodb.git', folder_name], cwd='../src/')
    subprocess.run(['cp', folder_name + '/.env.example', folder_name + '/.env'], cwd='../src/')
    subprocess.run(['docker-compose', 'exec', 'php', 'bash', '-c',
    'cd ' + folder_name + ' && composer install && php artisan key:generate'], cwd='../docker/')

def generateMicroserviceNginxConfig(folder, path):
    subprocess.run(['bash', 'microservice-template-inject.sh', folder, path])

def generateAll():
    subprocess.run(['rm', '-rf', 'services'], cwd='./nginx')
    subprocess.run(['mkdir', 'services'], cwd='./nginx')
    services = [
        service[:-8] 
        for service in os.listdir('../src')
        if service.endswith('-service')
    ]

    for service in services:
        generateMicroserviceNginxConfig(service + '-service', service)

parser = argparse.ArgumentParser(description='This program will generate Nginx configuration for your microservices.')

parser.add_argument('-a', '--all', action='store_true', 
 help='Create nginx config for all services and delete the old config files')


args, remining_args = parser.parse_known_args()

if(args.all):
    generateAll()
else:
    parser.add_argument('-b', '--use-boilerplate', action='store_true',
    help='Clone a new lumen project from boilerplate')
    parser.add_argument('folder_name', help='The name of the microservice folder')
    parser.add_argument('url_path', help='The path of the service in the Nginx configuration')
    parser.parse_args(remining_args)

    if(args.use_boilerplate):
        newLumenProject(args.folder_name)

    generateMicroserviceNginxConfig(args.folder_name, args.url_path)


subprocess.run(['docker-compose', 'restart', 'nginx'])
subprocess.run(['docker-compose', 'restart', 'php'])

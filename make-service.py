import argparse
import subprocess

def newLumenProject(folder_name):
    subprocess.run(['git', 'clone', 'https://github.com/3bdullahg97/lumen-mongodb.git', folder_name], cwd='../src/')
    subprocess.run(['cp', folder_name + '/.env.example', folder_name + '/.env'], cwd='../src/')
    proc = subprocess.run(['docker-compose', 'exec', 'php', 'bash', '-c',
    'cd ' + folder_name + ' && composer install && php artisan key:generate'], cwd='../docker/')

def generateMicroserviceNginxConfig(folder, path):
    subprocess.run(['bash', 'template-inject.sh', folder, path])

parser = argparse.ArgumentParser(description='This program will generate Nginx configuration for your microservices.')

parser.add_argument('-b', '--use-boilerplate', action='store_true',
 help='Clone a new lumen project from boilerplate')
parser.add_argument('folder_name', help='The name of the microservice folder')
parser.add_argument('url_path', help='The path of the service in the Nginx configuration')

args = parser.parse_args()

print(args)

if(args.use_boilerplate):
    newLumenProject(args.folder_name)

generateMicroserviceNginxConfig(args.folder_name, args.url_path)

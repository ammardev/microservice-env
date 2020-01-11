import argparse
import subprocess

parser = argparse.ArgumentParser(description='This program will generate Nginx configuration for your microservices.')

parser.add_argument('-p', '--http-port', help='Define the http port')
parser.add_argument('-P', '--https-port', help='Define the https port')
parser.add_argument('-r', '--root-path', help='Choose http root path')
parser.add_argument('-n', '--server-name', help='Choose server name (Hostname)')

args = parser.parse_args()

subprocess.run(['bash', 'nginx-config-inject.sh', args.http_port or "80"
 , args.https_port or "443", args.server_name or "localhost", args.root_path or "/var/www"])

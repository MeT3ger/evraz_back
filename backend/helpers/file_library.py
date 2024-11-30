import pathlib
from enum import Enum
import json

class Files(Enum):
    anubis = '2020.2-Anunbis-develop'
    backend_master = 'backend-master'
    donna_backend_master = 'donna-backend-master'
    final_year = 'final-year-project-backend-api-master'
    flask_postgres = 'Flask-PostgreSQL-API-Seed-master'
    flask_api = 'FlaskApiEcommerce-master'
    gramps_api = 'gramps-web-api-master'
    hacker_api =  'hackernews-api-main'
    http_api = 'http-api-3.1'
    launcher_api = 'luncher-api-master'
    ml_flask_api = 'ml-flask-api-master'
    rest_api = 'RESTfulAPI-master 2'

class FileLibrary:
        
    def get_file_path(filename: Files):
        return pathlib.Path('data', 'python', filename.value + '.zip')
    
    def get_json_path(filename: Files):
        return pathlib.Path('data', 'data_jsons', filename.value + '.json')
    
class GetDataBase:

    def get_db():
        jsons = ''

        with open(FileLibrary.get_json_path(Files.anubis), 'r') as file:
            data = json.load(file)
            jsons = jsons + '\n' + str(data)

        with open(FileLibrary.get_json_path(Files.backend_master), 'r') as file:
            data = json.load(file)
            jsons = jsons + '\n' + str(data)
        
        with open(FileLibrary.get_json_path(Files.donna_backend_master), 'r') as file:
            data = json.load(file)
            jsons = jsons + '\n' + str(data)
        
        with open(FileLibrary.get_json_path(Files.final_year), 'r') as file:
            data = json.load(file)
            jsons = jsons + '\n' + str(data)
        
        with open(FileLibrary.get_json_path(Files.flask_postgres), 'r') as file:
            data = json.load(file)
            jsons = jsons + '\n' + str(data)
        
        with open(FileLibrary.get_json_path(Files.flask_api), 'r') as file:
            data = json.load(file)
            jsons = jsons + '\n' + str(data)
        
        with open(FileLibrary.get_json_path(Files.gramps_api), 'r') as file:
            data = json.load(file)
            jsons = jsons + '\n' + str(data)
        
        with open(FileLibrary.get_json_path(Files.hacker_api), 'r') as file:
            data = json.load(file)
            jsons = jsons + '\n' + str(data)
        
        with open(FileLibrary.get_json_path(Files.http_api), 'r') as file:
            data = json.load(file)
            jsons = jsons + '\n' + str(data)
        
        with open(FileLibrary.get_json_path(Files.launcher_api), 'r') as file:
            data = json.load(file)
            jsons = jsons + '\n' + str(data)
        
        with open(FileLibrary.get_json_path(Files.ml_flask_api), 'r') as file:
            data = json.load(file)
            jsons = jsons + '\n' + str(data)
        
        with open(FileLibrary.get_json_path(Files.rest_api), 'r') as file:
            data = json.load(file)
            jsons = jsons + '\n' + str(data)

        return jsons
        
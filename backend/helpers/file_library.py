import pathlib
from enum import Enum

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
        return pathlib.Path('data', 'python', filename.value + '.json')
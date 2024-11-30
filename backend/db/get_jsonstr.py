from backend.db.file_library import FileLibrary, Files
import json

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
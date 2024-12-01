from backend.db.file_library import FileLibrary, Files
import json

class Database:

    def get():
        jsons = ''
        
        for file in Files:
            with open(FileLibrary.get_json_path(file), 'r') as f:
                data = json.load(f)
                jsons = jsons + '\n' + str(data)

        return jsons
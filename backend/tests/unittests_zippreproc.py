import unittest
import asyncio

from backend.parsers.zip_preproc import ZipPreproc
from backend.helpers.file_library import FileLibrary, Files

#Тест работоспособности класса
class TestZipPreproc(unittest.TestCase):
    
    def setUp(self):
        self.test_file_1 = ZipPreproc(FileLibrary.get_file_path(Files.anubis))
        self.test_file_2 = ZipPreproc(FileLibrary.get_file_path(Files.backend_master))
        self.test_file_3 = ZipPreproc(FileLibrary.get_file_path(Files.donna_backend_master))
        self.test_file_4 = ZipPreproc(FileLibrary.get_file_path(Files.final_year))
        self.test_file_5 = ZipPreproc(FileLibrary.get_file_path(Files.flask_postgres))
        self.test_file_6 = ZipPreproc(FileLibrary.get_file_path(Files.flask_api))
        self.test_file_7 = ZipPreproc(FileLibrary.get_file_path(Files.gramps_api))
        self.test_file_8 = ZipPreproc(FileLibrary.get_file_path(Files.hacker_api))
        self.test_file_9 = ZipPreproc(FileLibrary.get_file_path(Files.http_api))
        self.test_file_10 = ZipPreproc(FileLibrary.get_file_path(Files.launcher_api))
        self.test_file_11 = ZipPreproc(FileLibrary.get_file_path(Files.ml_flask_api))
        self.test_file_12 = ZipPreproc(FileLibrary.get_file_path(Files.rest_api))
    
    def test_create_json(self):
        
        #1 Тест с Anunbis-develop.zip
        try:
            asyncio.run(self.test_file_1.create_json(jsonname=FileLibrary.get_json_path(Files.anubis)))
        except Exception as e:
            self.fail(msg=f'Failed on Anunbis-develop.zip with {e}')

        #2 Тест с backend-master.zip
        try:   
            asyncio.run(self.test_file_2.create_json(jsonname=FileLibrary.get_json_path(Files.backend_master)))
        except Exception as e:
            self.fail(msg=f'Failed on backend-master.zip with {e}')
        
        #3 Тест с donna-backend-master.zip
        try:
            asyncio.run(self.test_file_3.create_json(jsonname=FileLibrary.get_json_path(Files.donna_backend_master)))
        except Exception as e:
            self.fail(msg=f'Failed on donna-backend-master.zip with {e}')
        
        #4 Тест с final-year-project-backend-api-master.zip
        try:
            asyncio.run(self.test_file_4.create_json(jsonname=FileLibrary.get_json_path(Files.final_year)))
        except Exception as e:
            self.fail(msg=f'Failed on final-year-project-backend-api-master.zip with {e}')
        
        #5 Тест с Flask-PostgreSQL-API-Seed-master.zip
        try:
            asyncio.run(self.test_file_5.create_json(jsonname=FileLibrary.get_json_path(Files.flask_postgres)))
        except Exception as e:
            self.fail(msg=f'Failed on Flask-PostgreSQL-API-Seed-master.zip with {e}')
        
        #6 Тест с FlaskApiEcommerce-master.zip
        try:
            asyncio.run(self.test_file_6.create_json(jsonname=FileLibrary.get_json_path(Files.flask_api)))
        except Exception as e:
            self.fail(msg=f'Failed on Flask-PostgreSQL-API-Seed-master.zip with {e}')
        
        #7 Тест с gramps-web-api-master.zip
        try:
            asyncio.run(self.test_file_7.create_json(jsonname=FileLibrary.get_json_path(Files.gramps_api)))
        except Exception as e:
            self.fail(msg=f'Failed on gramps-web-api-master.zip with {e}')
        
        #8 Тест с hackernews-api-main.zip
        try:
            asyncio.run(self.test_file_8.create_json(jsonname=FileLibrary.get_json_path(Files.hacker_api)))
        except Exception as e:
            self.fail(msg=f'Failed on hackernews-api-main.zip with {e}')
        
        # 9 Тест с http-api.zip
        try:
            asyncio.run(self.test_file_9.create_json(jsonname=FileLibrary.get_json_path(Files.http_api)))
        except Exception as e:
            self.fail(msg=f'Failed on http-api.zip with {e}')
        
        #10 Тест с luncher-api-master.zip
        try:
            asyncio.run(self.test_file_10.create_json(jsonname=FileLibrary.get_json_path(Files.launcher_api)))
        except Exception as e:
            self.fail(msg=f'Failed on luncher-api-master.zip with {e}')
        
        #11 Тест с ml-flask-api-master.zip
        try:
            asyncio.run(self.test_file_11.create_json(jsonname=FileLibrary.get_json_path(Files.ml_flask_api)))
        except Exception as e:
            self.fail(msg=f'Failed on ml-flask-api-master.zip with {e}')

        #12 Тест с RESTfulAPI-master.zip
        try:
            asyncio.run(self.test_file_12.create_json(jsonname=FileLibrary.get_json_path(Files.rest_api)))
        except Exception as e:
            self.fail(msg=f'Failed on RESTfulAPI-master {e}')
            
    '''    
    def test_find_file_types(self):

        #1 Тест с Anunbis-develop.zip
        res_func = asyncio.run(self.test_file_1.__find_file_types())
        res_true = set(['gitignore', 'Dockerfile', 'README', 'env', 
                    'Makefile', 'py', 'md', 'mako', 'pycodestyle', 'yml', 
                    'lock', 'png', 'dev', 'Procfile', 'html', 'sh', 'Pipfile', 
                    'txt', 'LICENSE', 'ini', 'json'])
        self.assertTrue(res_func == res_true, msg='Fail with Anunbis-develop.zip')

        #2 Тест с backend-master.zip
        res_func = asyncio.run(self.test_file_2.__find_file_types())
        res_true = set(['mako', 'yml', 'ini', 'md', 'mk', 'pylintrc', 
                       'py', 'Makefile', 'in', 'sh', 'toml', 'LICENSE', 
                       'gitignore', 'README', 'cfg'])
        self.assertTrue(res_func == res_true, msg='Fail with backend-master.zip')

        #3 Тест с donna-backend-master.zip
        res_func = asyncio.run(self.test_file_3.__find_file_types())
        res_true = set(['LICENSE', 'txt', 'db', 'py', 'gitignore', 'png', 'Procfile', 'md'])
        self.assertTrue(res_func == res_true, msg='Fail with donna-backend-master.zip')

        #4 Тест с final-year-project-backend-api-master.zip
        res_func = asyncio.run(self.test_file_4.__find_file_types())
        res_true = set(['prod', 'mako', 'lock', 'postman_collection', 
                       'sh', 'txt', 'dev', 'py', 'ini', 'xml', 'README', 
                       'gitignore', 'md', 'conf', 'Pipfile', 'env_sample', 'iml'])
        self.assertTrue(res_func == res_true, msg='Fail with final-year-project-backend-api-master.zip')

        #5 Тест с Flask-PostgreSQL-API-Seed-master.zip
        res_func = asyncio.run(self.test_file_5.__find_file_types())
        res_true = set(['LICENSE', 'py', 'yml', 'ini', 'mako', 
                       'txt', 'Dockerfile', 'Vagrantfile', 'gitignore', 'md', 'README'])
        self.assertTrue(res_func == res_true, msg='Fail with Flask-PostgreSQL-API-Seed-master.zip')

        #6 Тест с FlaskApiEcommerce-master.zip
        res_func = asyncio.run(self.test_file_6.__find_file_types())
        res_true = set(['iml', 'xml', 'png', 'gitignore', 'md', 'py', 'mako', 'README', 'ini', 'bat'])
        self.assertTrue(res_func == res_true, msg='Fail with FlaskApiEcommerce-master.zip')

        #7 Тест с gramps-web-api-master.zip
        res_func = asyncio.run(self.test_file_7.__find_file_types())
        res_true = set(['cfg', 'json', 'toml', 'iml', 'README', 
                       'xml', 'md', 'ini', 'py', 'onnx', 'mako', 'yml', 
                       'html', 'LICENSE', 'txt', 'flake8', 'gitignore', 
                       'pylintrc', 'sh', 'yaml', 'Dockerfile', 'editorconfig', 
                       'in', 'dockerignore'])
        self.assertTrue(res_func == res_true, msg='Fail with gramps-web-api-master.zip')

        #8 Тест с hackernews-api-main.zip
        res_func = asyncio.run(self.test_file_8.__find_file_types())
        res_true = set(['ini', 'README', 'test', 'mako', 
                       'production', 'Makefile', 'yaml', 'txt', 'json', 
                       'pylintrc', 'dockerignore', 'env', 'yml', 'conf', 'md', 
                       'j2', 'Procfile', 'editorconfig', 'sh', 'LICENSE', 'Dockerfile', 
                       'py', 'cfg', 'gitignore'])
        self.assertTrue(res_func == res_true, msg='Fail with hackernews-api-main.zip')

        #9 Тест с http-api.zip
        res_func = asyncio.run(self.test_file_9.__find_file_types())
        res_true = set(['whitesource', 'ini', 'pyi', 'typed', 
                       'sh', 'gitattributes', 'html', 'toml', 
                       'txt', 'yaml', 'Makefile', 'md', 'gitignore', 
                       'py', 'json', 'yml', 'bat', 'flake8', 'LICENSE', 'rst'])
        self.assertTrue(res_func == res_true, msg='Fail with http-api.zip')

        #10 Тест с luncher-api-master.zip
        res_func = asyncio.run(self.test_file_10.__find_file_types())
        res_true = set(['py', 'yml', 'txt', 'md', 'ini', 'xml', 'iml', 'gitignore', 'Dockerfile'])
        self.assertTrue(res_func == res_true, msg='Fail with luncher-api-master.zip')

        #11 Тест с ml-flask-api-master.zip
        res_func = asyncio.run(self.test_file_11.__find_file_types())
        res_true = set(['iml', 'rst', 'gitignore', 'nojekyll', 
                       'LICENSE', 'dockerignore', 'bat', 'cfg', 
                       'json', 'md', 'txt', 'Dockerfile', 'yml', 'env', 
                       'xml', 'py', 'Makefile'])
        self.assertTrue(res_func == res_true, msg='Fail with ml-flask-api-master.zip')

        #12 Тест с RESTfulAPI-master.zip
        res_func = asyncio.run(self.test_file_12.__find_file_types())
        res_true = set(['py', 'md', 'iml', 'xml', 'gitignore'])
        self.assertTrue(res_func == res_true, msg='Fail with RESTfulAPI-master.zip')
        '''

if __name__ == "__main__":
    unittest.main()
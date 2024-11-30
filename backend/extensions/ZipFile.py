from io import BytesIO
from backend.parsers.zip_preproc import ZipPreproc
from fastapi import UploadFile

class ZipFile:
    
    def __init__(self, file: UploadFile):
        self.file = file

    async def project_struct(self) -> str:
        file_content = await self.file.read()
        zip_arc = ZipPreproc(BytesIO(file_content))
        archieve = await zip_arc.fill_dict()
        return archieve
    
    async def get_project_type(self):
        file_content = await self.file.read()
        zip_arc = ZipPreproc(BytesIO(file_content))
        files_types = zip_arc.find_file_types()
        
        if 'py' in files_types:
            return 'python'
        elif 'cs' in files_types:
            return 'csharp'
        else:
            return 'typescript'
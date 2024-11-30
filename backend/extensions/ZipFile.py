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
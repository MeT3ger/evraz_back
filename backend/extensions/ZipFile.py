from io import BytesIO
from backend.parsers.zip_preproc import ZipPreproc
from fastapi import UploadFile

class ZipFile(UploadFile):

    async def to_dict(self):
        file_content = await self.read()
        zip_arc = ZipPreproc(BytesIO(file_content))
        archieve = await zip_arc.fill_dict()
        return archieve
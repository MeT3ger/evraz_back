# from backend.app.controllers import code_review
# from fastapi import File, HTTPException
# from backend.app.main import app
# from backend.extensions.ZipFile import ZipFile
    
# @app.post("/zip")
# async def zip(file: ZipFile = File(alias="some")):

#     if file.content_type != "application/zip":
#         raise HTTPException(status_code=400, detail="Uploaded file is not a ZIP archive.")
    
#     refactored_code = await code_review(file)
    
#     # dto = PDF_dto.json(refactored_code)
    
#     return refactored_code # dto
    
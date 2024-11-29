from langchain_community.document_loaders import PDFPlumberLoader
import asyncio

#Класс для парсинга пдф документа
class LoadPDF:

    def __init__(self):
        pass
    
    #Функция парсинга пдф файла
    #   filepath - путь до файла
    #Выходные данные:
    #   list[langchain_core.documents.Document] - список, содержащий данные о документе
    async def load_pdf(self, filepath):
        loader = PDFPlumberLoader(file_path=filepath,
                                extract_images=True
                                )
        return loader.load()
from langchain_community.document_loaders.pdf import PDFMinerLoader
import asyncio

#Класс для парсинга пдф документа
class LoadPDF:

    def __init__(self):
        pass
    
    #Функция парсинга пдф файла
    #   filepath - путь до файла
    #Выходные данные:
    #   list[langchain_core.documents.Document] - список, содержащий данные о документе
    def load_pdf(self, filepath):
        loader = PDFMinerLoader(
            file_path=filepath
        )
        return loader.load()[0].page_content
    
if __name__ == '__main__':
    print(LoadPDF().load_pdf('data\Instruct.pdf'))
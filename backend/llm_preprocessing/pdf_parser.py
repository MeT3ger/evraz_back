from langchain_community.document_loaders import PDFPlumberLoader
import asyncio

class LoadPDF:

    def __init__(self):
        pass

    async def load_pdf(self, filepath):
        loader = PDFPlumberLoader(
            file_path=filepath,
            extract_images=True
            )
        return loader.load()

if __name__ == '__main__':
    doc = LoadPDF()
    print(asyncio.run(doc.load_pdf(filepath='data\Instruct.pdf')))
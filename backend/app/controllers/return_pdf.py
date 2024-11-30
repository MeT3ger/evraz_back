import aspose.pdf as ap

import io
import asyncio
import shutil

class CreatePDF:
    
    async def create(json):
        pdf_buffer = io.BytesIO()
        string = json['choices'][0]['message']['content']
        document = ap.Document()
        page = document.pages.add()
        text_fragment = ap.text.TextFragment(string)
        page.paragraphs.add(text_fragment)
        document.save(pdf_buffer)

        return pdf_buffer
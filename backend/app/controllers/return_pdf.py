from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
import asyncio

class CreatePDF:
    async def create(json):
        pdf_buffer = io.BytesIO()
        canv = canvas.Canvas(pdf_buffer, pagesize=letter)
        string = json['choices'][0]['message']['content'].split('\n')
        x = 100
        y = 750
        for line in string:
            canv.drawString(x, y, line)
            y -= 15
        canv.save()
        pdf_buffer.seek(0)
        
        return pdf_buffer
'''
Пересылать будем примерно так:
pdf_name = 'document.pdf'
response = requests.post(url, files={'file': (pdf_name, pdf_buffer, 'application/pdf')})
'''
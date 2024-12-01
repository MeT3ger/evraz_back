from fpdf import FPDF

import io
import asyncio
import shutil

class CreatePDF:
    
    def create(json):
        pdf_buffer = io.BytesIO()
        string = json['choices'][0]['message']['content']

        pdf = FPDF()
        pdf.add_page()
        width = 180
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font('DejaVu', '', 12)
        pdf.multi_cell(width, 5, string)
        pdf_buffer.write(pdf.output(dest='S').encode('latin-1'))
        pdf_buffer.seek(0)
        # pdf_buffer = pdf.output(dest='S').encode('latin-1')
        #pdf.output('output.pdf', 'F')

        return pdf_buffer
    

if __name__ == '__main__':
    strin = 'Русский язык   фафафа \n'
    jsn = {'choices':[{'message':{'content':strin}}]}
    buff = asyncio.run(CreatePDF.create(jsn))
    file_location = 'output.pdf'

    with open(file_location, "wb") as file:
            file.write(buff)
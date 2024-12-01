from fpdf import FPDF
import io

class CreatePDF:
    
    def create(json):
        pdf_buffer = io.BytesIO()
        print(json)
        string = json['choices'][0]['message']['content']

        pdf = FPDF()
        pdf.add_page()
        width = 180
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font('DejaVu', '', 12)
        pdf.multi_cell(width, 5, string)
        pdf_buffer.write(pdf.output(dest='S').encode('latin-1'))
        pdf_buffer.seek(0)

        return pdf_buffer
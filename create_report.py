import os
from docx import Document
from docx.shared import Cm, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING

def create_report():
    # Initialize document
    doc = Document()
    
    # Set paper size to A4 (210 x 297 mm)
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    
    # Set Margins to 3 cm
    section.top_margin = Cm(3.0)
    section.bottom_margin = Cm(3.0)
    section.left_margin = Cm(3.0)
    section.right_margin = Cm(3.0)
    
    # Configure default style (Normal)
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Arial'
    font.size = Pt(12)
    
    # Configure Paragraph format
    paragraph_format = style.paragraph_format
    paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    paragraph_format.space_before = Pt(0)
    paragraph_format.space_after = Pt(0)
    
    # Identity Header
    doc.add_paragraph('Nama: Intan Bella Safira Putri Dewi')
    doc.add_paragraph('Kelas: III Rekayasa Perangkat Lunak Kripto')
    doc.add_paragraph('NPM: 2322101923')
    doc.add_paragraph() # empty line
    
    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_title = p_title.add_run('LAPORAN TUGAS PRAKTIKUM\nPENGUJIAN PERANGKAT LUNAK (LOGIN & REGISTER)')
    run_title.bold = True
    doc.add_paragraph()
    
    # 1. Test Case Section
    p_h1 = doc.add_paragraph()
    run_h1 = p_h1.add_run('1. Skenario Test Case (Login & Register)')
    run_h1.bold = True
    
    doc.add_paragraph('Berikut adalah skenario test case untuk modul Register dan Login pada aplikasi quiz-pengupil.')
    
    # Adding Test Case table from testcases.md
    try:
        with open('tests/testcases.md', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                doc.add_paragraph(line.strip())
    except FileNotFoundError:
        doc.add_paragraph('[ISI TABEL TEST CASE DI SINI]')
        
    doc.add_paragraph()
    
    # 2. Selenium Script Section
    p_h2 = doc.add_paragraph()
    run_h2 = p_h2.add_run('2. Implementasi Automation Testing (Selenium)')
    run_h2.bold = True
    
    doc.add_paragraph('Script di bawah ini dirancang untuk dijalankan menggunakan mode Headless agar kompatibel dengan lingkungan server CI/CD. Pengujian juga menggunakan teknik Stubbing pada CI/CD dengan cara me-replace variabel konfigurasi koneksi menggunakan perintah sed.')
    doc.add_paragraph()
    doc.add_paragraph('[ISI SCREENSHOT ATAU KODE PYTHON DI BAWAH INI]')
    
    try:
        with open('tests/test_auth.py', 'r', encoding='utf-8') as f:
            code = f.read()
            doc.add_paragraph(code)
    except FileNotFoundError:
        doc.add_paragraph('[KODE PYTHON DI SINI]')
        
    doc.add_paragraph()
    
    # 3. CI/CD Section
    p_h3 = doc.add_paragraph()
    run_h3 = p_h3.add_run('3. Penerapan CI/CD Pipeline (Github Actions)')
    run_h3.bold = True
    
    doc.add_paragraph('Penerapan CI/CD berhasil dilakukan. Github Actions telah dikonfigurasi untuk menyiapkan Service Container (MySQL), PHP, instalasi dependensi, dan menjalankan file testing otomatis.')
    doc.add_paragraph()
    doc.add_paragraph('[MASUKKAN SCREENSHOT CI/CD GITHUB ACTIONS BERHASIL (CENTANG HIJAU) DI SINI]')
    doc.add_paragraph('[MASUKKAN SCREENSHOT LOG EKSEKUSI SELENIUM ("Ran 4 tests in ... OK") DI SINI]')
    doc.add_paragraph('[MASUKKAN SCREENSHOT LOG "Setup MySQL database" DI SINI]')

    # Save Document
    doc.save('2322101923_Intan Bella Safira Putri Dewi_Kuis.docx')
    print("Document successfully created!")

if __name__ == '__main__':
    create_report()

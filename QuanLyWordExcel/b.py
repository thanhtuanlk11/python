from docx import Document 

document = Document()

# số 0 là size chữ
document.add_heading('Giấy mời họp phụ huynh', 0)

p = document.add_paragraph('Học sinh: ')
p.add_run("Nam").bold = True  
p.add_run(" - Lớp 10").italuc = True;


document.save("text.docx")
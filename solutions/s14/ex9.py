from pypdf import PdfReader, PdfWriter

reader = PdfReader("merged.pdf")
writer = PdfWriter()
for i in (0, 2):  # 1쪽과 3쪽 (번호는 0부터)
    writer.add_page(reader.pages[i])
writer.write("picked.pdf")
print("picked.pdf", len(writer.pages), "쪽")

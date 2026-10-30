from pathlib import Path

from pypdf import PdfReader, PdfWriter

writer = PdfWriter()
for path in sorted(Path("pdfs").glob("*.pdf")):
    writer.append(path)
    print("붙였어요:", path.name)
writer.write("merged.pdf")
print("모두", len(writer.pages), "쪽")

reader = PdfReader("merged.pdf")
print(reader.pages[3].extract_text())

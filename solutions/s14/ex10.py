from pathlib import Path

from pypdf import PdfReader

for path in sorted(Path("pdfs").glob("*.pdf")):
    reader = PdfReader(path)
    first_line = reader.pages[0].extract_text().splitlines()[0]
    print(path.name, len(reader.pages), "쪽 ·", first_line)

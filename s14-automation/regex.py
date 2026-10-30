import re

memo = """회의 참석자 연락처
김민지 010-1234-5678 minji@example.com
이준호 010-9876-5432 junho@example.org
다음 회의는 11월 5일"""

phones = re.findall(r"\d{3}-\d{4}-\d{4}", memo)
print(phones)

emails = re.findall(r"[\w.]+@[\w.]+", memo)
print(emails)

masked = re.sub(r"(\d{3})-\d{4}-(\d{4})", r"\1-****-\2", memo)
print(masked)

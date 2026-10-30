import re

log = """12:01 ERROR db timeout
12:05 INFO ok
12:09 ERROR disk full"""

for m in re.finditer(r"(\d{2}:\d{2}) ERROR (.+)", log):
    print(m.group(1), "|", m.group(2))

m = re.search(r"(?P<user>[\w.]+)@(?P<domain>[\w.]+)", "문의: dante@example.com")
print(m["user"], m["domain"])


def is_phone(text: str) -> bool:
    return re.fullmatch(r"010-\d{4}-\d{4}", text) is not None


for t in ["010-1234-5678", "010-12-5678", "010-1234-56789"]:
    print(t, is_phone(t))

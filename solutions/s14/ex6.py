import re

lines = ["[WARN] 12:30 disk 85%", "[ERROR] 12:31 disk full"]
for line in lines:
    m = re.fullmatch(r"\[(?P<level>\w+)\] (?P<time>\d{2}:\d{2}) (?P<text>.+)", line)
    if m:
        print(m["level"], m["time"], m["text"])

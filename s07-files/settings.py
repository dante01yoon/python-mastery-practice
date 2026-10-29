import json

settings = {"이름": "민지", "글자 크기": 14, "어두운 화면": True, "최근 파일": ["a.txt", "b.txt"]}

text = json.dumps(settings, ensure_ascii=False, indent=2)
print(text)

with open("settings.json", "w", encoding="utf-8") as f:
    json.dump(settings, f, ensure_ascii=False, indent=2)

with open("settings.json", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded["글자 크기"] + 2)
print(loaded["최근 파일"][0])

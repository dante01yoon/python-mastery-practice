import json

movies = [{"제목": "기생충", "연도": 2019}, {"제목": "올드보이", "연도": 2003}, {"제목": "괴물", "연도": 2006}]
with open("movies.json", "w", encoding="utf-8") as f:
    json.dump(movies, f, ensure_ascii=False, indent=2)

with open("movies.json", encoding="utf-8") as f:
    loaded = json.load(f)
print(max(loaded, key=lambda m: m["연도"])["제목"])

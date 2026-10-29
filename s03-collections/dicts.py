# 딕셔너리·튜플·집합: 수업에서 한 줄씩 친 코드
student = {"name": "단테", "age": 31}
print(student["name"])
student["city"] = "서울"
student["age"] = 32
print(student)
print(student.get("phone", "없음"))

point = (3, 5)
x, y = point
print(x, y)

tags = {"파이썬", "uv", "파이썬"}
print(tags)
tags.add("코딩")
print(len(tags))

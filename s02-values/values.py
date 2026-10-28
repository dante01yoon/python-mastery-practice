# 4편 · 값과 변수: 수업에서 한 줄씩 친 코드
age = 31
height = 175.5
name = "단테"
is_student = False
print(type(age), type(height), type(name), type(is_student))

print(f"{name}님은 {age}살, 키 {height}cm")
age = age + 1
print(age)

num = input("좋아하는 숫자: ")
print(num * 2)       # 문자열이라 두 번 이어 붙는다
print(int(num) * 2)  # 숫자로 바꿔야 계산된다

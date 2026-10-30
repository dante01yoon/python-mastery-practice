a = 7
b = 3
print(a == b, a != b)
print(a > b, a <= b)
print(0 < a < 10)

age = 25
has_ticket = True
print(age >= 19 and has_ticket)
print(age < 13 or age >= 65)
print(not has_ticket)

print("py" in "python", "java" not in "python")
result = None
print(result is None)
label = "성인" if age >= 19 else "미성년"
print(label)
print(2 + 3 * 4, (2 + 3) * 4)

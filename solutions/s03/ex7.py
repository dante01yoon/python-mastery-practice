a = [1, 2]
b = a
c = a.copy()
a.append(3)
print(b)  # [1, 2, 3]: b는 a와 같은 상자
print(c)  # [1, 2]: c는 복사한 새 상자

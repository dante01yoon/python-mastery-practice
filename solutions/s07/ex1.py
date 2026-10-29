with open("todo.txt", "w", encoding="utf-8") as f:
    f.write("장보기\n운동\n파이썬 복습\n")

with open("todo.txt", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        print(i, line.strip())

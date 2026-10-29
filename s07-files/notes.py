with open("diary.txt", "w", encoding="utf-8") as f:
    f.write("오늘 파이썬으로 파일을 만들었다.\n")
    f.write("내일은 CSV를 배운다.\n")

with open("diary.txt", "a", encoding="utf-8") as f:
    f.write("한 줄 더 붙였다.\n")

with open("diary.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

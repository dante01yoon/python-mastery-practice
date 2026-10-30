from collections import Counter

text = "파이썬으로 파일을 정리하면 퇴근이 빨라진다"
print(Counter(text.replace(" ", "")).most_common(3))

questions = [
    ("파이썬을 만든 사람은?", "귀도"),
    ("리스트 첫 칸의 번호는?", "0"),
    ("딕셔너리는 값을 무엇으로 찾을까?", "키"),
]
score = 0

for question, answer in questions:
    reply = input(question + " ")
    if reply == answer:
        print("정답!")
        score += 1
    else:
        print(f"땡! 정답은 {answer}")

print(f"{len(questions)}문제 중 {score}개 맞혔어요")

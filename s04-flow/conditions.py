# 조건문: 수업에서 한 줄씩 친 코드
score = int(input("점수: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("다시 도전!")

command = input("명령: ")
match command:
    case "시작":
        print("게임을 시작합니다")
    case "종료":
        print("안녕히 가세요")
    case _:
        print("모르는 명령이에요")

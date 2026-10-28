# 미니 프로젝트 1: Madlibs(빈칸 채우기 이야기)
adjective = input("형용사 하나: ")
place = input("장소 하나: ")
food = input("음식 하나: ")
count = int(input("숫자 하나: "))

story = f"오늘 나는 {adjective} 기분으로 {place}에 갔다. 거기서 {food}을(를) {count}개나 먹었다! 다음엔 {count * 2}개에 도전!"
print(story)

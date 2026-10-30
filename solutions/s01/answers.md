# 풀이 · Git·GitHub 첫걸음

## 1
```bash
git clone https://github.com/dante01yoon/python-mastery-practice
cd python-mastery-practice
git log --oneline -3      # -3: 최근 세 개만
```
메시지는 저장소가 바뀔 때마다 달라집니다. 맨 위가 가장 최근이에요.

## 2
```bash
mkdir my-notes && cd my-notes
git init
echo "오늘 배운 것: git init" > memo.txt
git add memo.txt
git commit -m "메모 시작"
echo "오늘 배운 것: git commit" >> memo.txt
git add memo.txt
git commit -m "메모 한 줄 추가"
git log --oneline         # 두 줄
```
`>`는 파일을 새로 쓰고, `>>`는 끝에 덧붙입니다.

## 3
```bash
echo "지울 줄" >> memo.txt
git diff                  # + 지울 줄
git restore memo.txt      # 마지막 커밋 상태로
git diff                  # 아무것도 안 나오면 되돌아간 것
```

# Git·GitHub 첫걸음 — 수업에서 친 명령

처음 한 번만 (내 이름과 GitHub에 쓰는 이메일로 바꿔서):

```bash
git config --global user.name "내 이름"
git config --global user.email "내-이메일@example.com"
git config --global init.defaultBranch main
```

Windows는 https://git-scm.com 에서 Git을 먼저 설치하세요. macOS는 터미널에서 `git --version`을 치면 설치 안내가 나옵니다.

저장점 만들기:

```bash
mkdir my-first && cd my-first
git init                  # 이 폴더를 Git에게 맡기기
git status                # 지금 상태
git add hello.py          # 저장할 파일 담기
git commit -m "첫 저장"   # 저장점 만들기
git log --oneline         # 저장점 기록
git diff                  # 마지막 저장점과 지금 비교
```

실습 저장소 받기와 새로 받기:

```bash
git clone https://github.com/dante01yoon/python-mastery-practice
cd python-mastery-practice
git pull                  # 새로 올라온 저장점 받기
```

내 저장소에 올리기(push)는 GitHub에서 빈 저장소를 만들고 로그인한 뒤, GitHub가 보여 주는 `git remote add origin …`, `git push -u origin main` 두 줄을 그대로 실행하면 됩니다.

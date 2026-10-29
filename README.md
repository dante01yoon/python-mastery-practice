# 파이썬 완전정복 — 실습 저장소

강의에서 친 코드, 미니 프로젝트, 연습문제와 풀이.

| 폴더 | 내용 |
|---|---|
| `s02-values/` | 값과 변수(`values.py`), 미니 프로젝트 매드립스·단위 변환기 |
| `s03-collections/` | 리스트(`lists.py`), 딕셔너리·튜플·집합(`dicts.py`) |
| `s04-flow/` | 조건문·반복문, 미니 프로젝트 숫자 맞히기(`guess.py`)·가위바위보(`rps.py`)·퀴즈(`quiz.py`)·쇼핑 카트(`cart.py`) |
| `s05-functions/` | 함수(`functions.py`), 인자·타입 힌트(`args.py`), 스코프·람다·재귀(`scope.py`), 미니 프로젝트 행맨(`hangman.py`) |
| `s06-exceptions/` | 오류 추적 읽기(`errors.py`), try/except/else/finally(`safe_input.py`), raise·사용자 예외(`raise_demo.py`), 디버거 실습(`debug_me.py` — 영상은 `total = price` 실수로 시작해 `+=`로 고친다, 디버거 설정은 `.vscode/launch.json`), 미니 프로젝트 은행(`bank.py`) |
| `s07-files/` | 텍스트 파일(`notes.py`), pathlib(`paths.py`), CSV 가계부(`budget.py`·`spending.csv`), JSON(`settings.py`), 미니 프로젝트 비밀번호 관리자(`vault.py` — 연습용, 실제 비밀번호 금지) |
| `exercises/` | 섹션별 연습문제 |
| `solutions/` | 풀이 |

## 설치 (uv + 파이썬 3.15)

macOS · Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

그다음:

```bash
uv python install 3.15
uv run s02-values/madlibs.py
```

> uv 0.13부터 `uv init`은 기본으로 패키지 구조(`src/`)를 만듭니다. 강의 첫 프로젝트는 파일 하나로 시작하려고 `uv init --no-package hello`를 씁니다.

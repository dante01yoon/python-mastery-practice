# 파이썬 완전정복 — 실습 저장소

강의에서 친 코드, 미니 프로젝트, 연습문제와 풀이.

| 폴더 | 내용 |
|---|---|
| `s02-values/` | 값과 변수(`values.py`), 미니 프로젝트 매드립스·단위 변환기 |
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

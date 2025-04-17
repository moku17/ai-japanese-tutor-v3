🇺🇸eng

# AI Japanese Tutor

This is a web application for learning Japanese for Korean users.
It randomly presents problems in the areas of grammar, reading, vocabulary, and kanji, and analyzes the user's correct answer rate and weaknesses to suggest a learning direction.

## Key Features

- 2 questions each from grammar, reading comprehension, vocabulary, and Chinese characters (8 questions total)
- Correct answer rate and weak area analysis
- Simple web UI based
- Includes commentary function (some automatic commentary available)

## How to run

1. After cloning the project, install the required packages.
2. The commentary feature is enabled by creating a `.env` file and entering your OpenAI API key.
3. After running it with the `python app.py` command, you can use it by accessing `http://127.0.0.1:5000` in your browser.

## Technology used

- Python (Flask)
- HTML, CSS
- Problem structure based on JSON data

## Folder organization

- `app.py`: Server execution main file
- `templates/`: Problem and Results Page Template
- `data/problems.json`: Problem Data Repository
- `static/style.css`: Basic style file




🇰🇷kor

# AI 일본어 튜터

한국어 사용자를 위한 일본어 학습용 웹 애플리케이션입니다.  
문법, 독해, 어휘, 한자 영역의 문제를 랜덤으로 출제하고, 사용자의 정답률과 약점을 분석하여 학습 방향을 제시합니다.

## 주요 기능

- 문법, 독해, 어휘, 한자 문제 각 2문제씩 출제 (총 8문제)
- 정답률 및 약점 영역 분석
- 간단한 웹 UI 기반
- 해설 기능 포함 (일부 자동 해설 제공 가능)

## 실행 방법

1. 프로젝트를 클론한 후 필요한 패키지를 설치합니다.
2. `.env` 파일을 생성하고 OpenAI API 키를 입력하면 해설 기능이 활성화됩니다.
3. `python app.py` 명령어로 실행 후, 브라우저에서 `http://127.0.0.1:5000` 으로 접속하여 사용할 수 있습니다.

## 사용 기술

- Python (Flask)
- HTML, CSS
- JSON 데이터 기반 문제 구조

## 폴더 구성

- `app.py`: 서버 실행 메인 파일
- `templates/`: 문제와 결과 페이지 템플릿
- `data/problems.json`: 문제 데이터 저장소
- `static/style.css`: 기본 스타일 파일

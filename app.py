import os
import openai
import json
import random
from dotenv import load_dotenv
from flask import Flask, render_template, request, session

# 환경 변수 로드
load_dotenv()
print("불러온 키:", os.getenv("OPENAI_API_KEY"))
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
app.secret_key = "supersecret"  # 세션용 키

# 문제 불러오기
def load_questions():
    with open("data/problems.json", "r", encoding="utf-8") as f:
        all_questions = json.load(f)
    return random.sample(all_questions, 8)

# GPT 해설 생성
def generate_explanation(question_text, correct_answer):
    prompt = f"""
    다음 일본어 문제에 대해 해설을 작성해 주세요.

    문제: {question_text}
    정답: {correct_answer}

    한국어로 간결하고 명확하게 설명해 주세요. 학습자 수준은 초중급입니다.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"(해설 생성 실패: {e})"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        all_questions = json.loads(session.get("questions", "[]"))

        score = 0
        result = []
        type_wrong = {}

        for q in all_questions:
            user_ans = request.form.get(q["id"])
            correct = (user_ans == q["answer"])

            explanation = ""
            if not correct:
                explanation = generate_explanation(q["question"], q["answer"])

            if correct:
                score += 1

            result.append({
                "id": q["id"],
                "question": q["question"],
                "user_ans": user_ans,
                "correct_ans": q["answer"],
                "correct": correct,
                "type": q["type"],
                "explanation": explanation
            })

            if not correct:
                type_wrong[q["type"]] = type_wrong.get(q["type"], 0) + 1

        weaknesses = list(type_wrong.keys())
        return render_template("result.html", score=score, total=8, result=result, weaknesses=weaknesses)

    else:
        questions = load_questions()
        session["questions"] = json.dumps(questions, ensure_ascii=False)
        return render_template("index.html", questions=questions)

if __name__ == "__main__":
    app.run(debug=True)
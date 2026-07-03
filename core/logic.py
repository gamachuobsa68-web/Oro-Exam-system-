from data.questions import QUESTIONS

def grade_exam(answers):
    score = 0

    for i, q in enumerate(QUESTIONS):
        if i < len(answers) and answers[i] == q["answer"]:
            score += 1

    total = len(QUESTIONS)
    return score, total
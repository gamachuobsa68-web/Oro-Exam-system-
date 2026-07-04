from data.questions import QUESTIONS

def grade_exam(answers):

    score = 0

    for i in range(len(QUESTIONS)):

        if i < len(answers):

            if answers[i] == QUESTIONS[i]["answer"]:
                score += 1

    return score, len(QUESTIONS)
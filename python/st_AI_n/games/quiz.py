import random


def quiz():
    points = 0

    questions = [
        "what is the best food in the entire universe"
    ]

    answers = [
        "bread"
    ]

    for i in range(len(questions)):
        chosen_question = random.choice(questions)
        correct_answer = answers[questions.index(chosen_question)]

        print(chosen_question)
        user_answer = input().lower()

        if user_answer == correct_answer:
            print("correct")
            points += 1
        else:
            print("incorrect")

        questions.remove(chosen_question)
        answers.remove(correct_answer)

    print(f"your score is {points} points")
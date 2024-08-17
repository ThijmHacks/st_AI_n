import random


def quiz():
    score = 0

    questions = [
        "what is the best food in the entire universe?",
        "from 1-10, what is my favorite number?",
        "what is the best movie ever made?",
        "what is the best drink?",
        "what is my favorite animal?",
        "what is my favorite car?",
        "grated cheese",
        "who am i married to"
    ]

    answers = [
        "bread",
        "1",
        "cars 2",
        "vodka",
        "nyctibius",
        "bike",
        "grated cheese",
        "rock"
    ]

    for i in range(len(questions)):
        chosen_question = random.choice(questions)
        correct_answer = answers[questions.index(chosen_question)]

        user_answer = input(chosen_question + "\n").lower()

        if user_answer == correct_answer:
            print("correct\n")
            score += 1
        else:
            print("incorrect\n")

        questions.remove(chosen_question)
        answers.remove(correct_answer)

    if score == 1:
        print(f"your score is {score} point")
    elif score == int(len(questions)):
        print("go touch grass")
    else:
        print(f"your score is {score} points")

    quit()


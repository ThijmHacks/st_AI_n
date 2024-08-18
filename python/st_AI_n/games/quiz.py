import random


def quiz():
    if random.randint(1, 2) == 1:
        quiz_1()
    else:
        quiz_2()

def quiz_1():
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


def quiz_2():
    score = 0

    questions = [
        "what is the most used operating system in the world",
        "what is the worst programming language ever made",
        "what linux distro makes you a femboy",
        "is python statically typed or dynamically typed",
        "in what year did google buy android",
        "who created the linux kernel",
        "who made python",
        "what is another name for robots who visit websites searching for information",
        "what popular old operating system is macos based on",
        "what company makes a lot of popular IDEs (integrated development environments)",
        "what company made the programming language swift",
        "what is the most popular programming language, as of 2024?",
        "is c an object oriented programming language",
        "is c++ an object oriented programming language"
    ]

    answers = [
        "windows",
        "c++",
        "arch",
        "dynamically",
        "2005",
        "linus torvalds",
        "guido van rossum",
        "spiders",
        "unix",
        "jetbrains",
        "apple",
        "javascript",
        "no",
        "yes"
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
# -------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECTO!")
        return 1
    else:
        print("INCORRECTO!")
        return 0


# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTADO")
    print("-------------------------")

    print("Claves: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Respondidas: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
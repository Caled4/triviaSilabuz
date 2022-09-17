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

    score = int((correct_guesses / len(questions)) * 100)
    print("tu puntaje es: " + str(score) + "%")


# -------------------------
def play_again():

    response = input("quieres jugar de nuevo? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


# -------------------------

questions = {
    "¿En qué galaxia se encuentra el sistema solar?: ": "A",
    "que estacion del anho es mas helado?: ": "B",
    "Python es homenajeado a qué grupo de comedia?: ": "C",
    "la tierra es redonda?: ": "A"
}

options = [[
    "A. Via lactea", "B. Via gasosa", "C. via cholate", "D. reino funji"
], ["A. primaver", "B. invierno", "C. verano", "D. otonho"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. si ", "B. no", "C. talves", "D. que es la tierra?"]]

new_game()

while play_again():
    new_game()

print("Byeeeeee!")
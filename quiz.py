import random

# Labels used for multiple-choice answers
LABELS = [1, 2, 3, 4]




def questions_db():
    """
      Creates and returns the question database.
      Each question is a dictionary with:
          - "question": the question text (string)
          - "options": 4 possible answers (list of 4 strings)
          - "answer": the correct answer (string)
    """
    questions_list = [
        {
            "question": "Which Brazilian city is famous for the Christ the Redeemer statue?",
            "options": ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador"],
            "answer": "Rio de Janeiro"
        },
        {
            "question": "Brazil has the largest Japanese community outside Japan. Which city is it most concentrated in?",
            "options": ["Curitiba", "Manaus", "São Paulo", "Recife"],
            "answer": "São Paulo"
        },
        {
            "question": "Approximately what percentage of the Amazon Rainforest is in Brazilian territory?",
            "options": ["20%", "60%", "40%", "80%"],
            "answer": "60%"
        },
        {
            "question": "Which festival is world-famous and attracts millions of tourists every year?",
            "options": ["Festa do Peão de Barretos", "São João de Campina Grande", "Rio de Janeiro Carnival", "Oktoberfest of Blumenau"],
            "answer": "Rio de Janeiro Carnival"
        },
        {
            "question": "Feijoada is a famous Brazilian dish. What is the main ingredient?",
            "options": ["Chicken", "Fish", "Rice and vegetables", "Beef and pork with black beans"],
            "answer": "Beef and pork with black beans"
        },
        {
            "question": "What is the current capital city of Brazil?",
            "options": ["Buenos Aires", "Brasília", "Rio de Janeiro", "Salvador"],
            "answer": "Brasília"
        },
        {
            "question": "What is the official language of Brazil?",
            "options": ["Spanish", "English", "Portuguese", "French"],
            "answer": "Portuguese"
        },
        {
            "question": "How many times has Brazil won the FIFA World Cup?",
            "options": ["3 times", "4 times", "5 times", "6 times"],
            "answer": "5 times"
        },
        {
            "question": "Iguazu Falls are on the border of Brazil and which other country?",
            "options": ["Argentina", "Venezuela", "Colombia", "Peru"],
            "answer": "Argentina"
        },
        {
            "question": "What is the currency used in Brazil?",
            "options": ["Peso", "Real", "Dollar", "Escudo"],
            "answer": "Real"
        },
        {
            "question": "Which is the biggest state in Brazil by area?",
            "options": ["Amazonas", "São Paulo", "Bahia", "Paraná"],
            "answer": "Amazonas"
        },
        {
            "question": "Which ocean borders Brazil on the east coast?",
            "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
            "answer": "Atlantic Ocean"
        },
        {
            "question": "Which famous Brazilian sport uses a ball and players try to score goals?",
            "options": ["Cricket", "Football (Soccer)", "Baseball", "Rugby"],
            "answer": "Football (Soccer)"
        },
        {
            "question": "What is the name of the long river that is very famous in Brazil and South America?",
            "options": ["Nile River", "Amazon River", "Thames River", "Danube River"],
            "answer": "Amazon River"
        },
        {
            "question": "Which Brazilian city is known for its large carnival celebrations besides Rio de Janeiro?",
            "options": ["Salvador", "Brasília", "Curitiba", "Goiânia"],
            "answer": "Salvador"
        },
        {
            "question": "What is the main language spoken in Brazil?",
            "options": ["Spanish", "Portuguese", "French", "Italian"],
            "answer": "Portuguese"
        },
        {
            "question": "Which Brazilian region is known for being the driest in some areas?",
            "options": ["North", "Northeast", "South", "Southeast"],
            "answer": "Northeast"
        },
        {
            "question": "Which Brazilian city is famous for its modern government buildings and planned design?",
            "options": ["Brasília", "Recife", "Fortaleza", "Belém"],
            "answer": "Brasília"
        },
        {
            "question": "What is a popular Brazilian music style often linked to samba and carnival?",
            "options": ["Samba", "K-Pop", "Reggae", "Opera"],
            "answer": "Samba"
        },
        {
            "question": "What is a common Brazilian drink made from sugar cane?",
            "options": ["Tea", "Cachaça", "Milk", "Orange Juice"],
            "answer": "Cachaça"
        },
        {
            "question": "Which Brazilian animal is a big cat found in forests and wetlands?",
            "options": ["Polar Bear", "Jaguar", "Kangaroo", "Tiger"],
            "answer": "Jaguar"
        },
        {
            "question": "What is the name of the big wetland area in Brazil, famous for wildlife?",
            "options": ["Sahara", "Pantanal", "Alps", "Gobi"],
            "answer": "Pantanal"
        },
        {
            "question": "Which of these is a famous Brazilian snack made of cheese bread balls?",
            "options": ["Sushi", "Pão de queijo", "Tacos", "Croissant"],
            "answer": "Pão de queijo"
        },
        {
            "question": "Which Brazilian holiday happens in February or March and includes parades and costumes?",
            "options": ["Christmas", "Carnival", "Easter", "Halloween"],
            "answer": "Carnival"
        },
        {
            "question": "Which Brazilian city is the largest by population?",
            "options": ["Brasília", "São Paulo", "Florianópolis", "Natal"],
            "answer": "São Paulo"
        },
        {
            "question": "Which Brazilian region is the coldest and has more European influence in some cities?",
            "options": ["North", "Northeast", "South", "Center-West"],
            "answer": "South"
        },
        {
            "question": "What is the name of the Brazilian dance and martial art often played in a circle?",
            "options": ["Capoeira", "Ballet", "Hip-hop", "Salsa"],
            "answer": "Capoeira"
        },
        {
            "question": "Which famous Brazilian writer wrote 'The Alchemist'?",
            "options": ["Paulo Coelho", "Machado de Assis", "Clarice Lispector", "Jorge Amado"],
            "answer": "Paulo Coelho"
        },
        {
            "question": "Which Brazilian flag color is NOT on the flag?",
            "options": ["Green", "Yellow", "Blue", "Purple"],
            "answer": "Purple"
        },
        {
            "question": "Which Brazilian city is famous for the beach called Copacabana?",
            "options": ["Rio de Janeiro", "Recife", "Porto Alegre", "Manaus"],
            "answer": "Rio de Janeiro"
        }
    ]
    return questions_list




# Ask user's name, if he don't put the name, the standard will be "Player"
def get_player_name():
    name = input("What is your name? ")
    if name == "":
        name = "Player"
    return name

# Ask if the user want to see if his answer was correct or incorrect after answer the question or only in the end
def get_if_player_want_answer():

    answer = input(
        "Would you like to know if you got a correct or incorrect answer after each question \nor only check the result in the end? (1 for YES or 2 to check In the end? ")

    while True:
        if answer == "1":
            return True

        elif answer == "2":
            return False
        else:
            answer =  input("Invalid choice, try again, 1 for YES or 2 to check In the end. ")


# Ask how many questions the user wants to answer in the quiz
def get_how_many_questions(total_questions):
    while True:
        user_input = input(f"How many questions would you like to answer?  (1 to {total_questions}) ")
        if user_input.isdigit():
            number = int(user_input)
            if number >= 1 and number <= total_questions:
                return number
            else:
                print(f"Please enter a number from 1 to {total_questions}")
        else:
            print("Please enter a valid number")

# Choose random questions from the DB according to the number entered by user
def choose_questions(questions_db, number_of_questions):
    sample = random.sample(questions_db, number_of_questions)
    return sample


# Make answers random from the random list (choose_questions)
def randomize(answer_list):
    random.shuffle(answer_list)
    return answer_list

# Ask the user for 1/2/3/4 and keep asking until it is valid.
def user_answer():
    while True:
        choice = input(f"Your answer (1, 2, 3, or 4): ")
        if choice.isdigit():
            choice = int(choice)
            if choice in LABELS:
                return choice
        print("Invalid. Please enter a valid answer")
    return

# If user chose to see the answer after each question, this function will show the answer
def display_answer(display_correct_incorrect, user_choice, correct_choice):
    if display_correct_incorrect:
        if user_choice == correct_choice:
            print(f"Your answer {user_choice} was correct")
        else:
            print(f"Your answer {user_choice} was NOT correct")



#display the question for the user, one at time
def display_question(question_dict, amount, display_correct_incorrect):
    print("\n...........................")
    print("\n")
    print(f"Question: {amount}: {question_dict['question']}")

    options = randomize(question_dict['options'])

    correct_index = options.index(question_dict['answer'])
    correct_label = correct_index + 1

    for i in range(len(LABELS)):
        print(f"{LABELS[i]}: {options[i]}")

    choice = user_answer()

    display_answer(display_correct_incorrect, choice, correct_label)

    return choice == correct_label


# Runs through all questions, counts how many are correct, and returns the score
def quiz_start(questions, display_correct_incorrect):
    score = 0

    for i, question in enumerate(questions, 1):
        if display_question(question, i, display_correct_incorrect):
            score += 1
    return score


def main():

    questions = questions_db()
    print("Welcome to the Holton College Quiz about Brazil")

    name = get_player_name()
    display_correct_incorrect = get_if_player_want_answer()
    how_many = get_how_many_questions(len(questions))
    questions_to_ask = choose_questions(questions, how_many)


    score = quiz_start(questions_to_ask, display_correct_incorrect)

    percent = (score / how_many) * 100
    print("\n============================")
    print("Quiz finished!")
    print(f"{name}, your score: {score} out of {how_many}")
    print(f"Percentage: {percent:.2f}%")
    print("============================")
    print("\n")


    while True:
        play_again = input("Would you like to play again? (1 for YES or 2 to END?) ")
        if play_again == "1":
            main()
        elif play_again == "2":
            break
        else:
            print("Please enter a valid answer")


main()



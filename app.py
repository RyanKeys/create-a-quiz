# instantiate questions here
# dict keys = {"YOUR_ANSWER_HERE":"YOUR_QUESTION_HERE"}
questions = [
    {"a": "2+2 = ? \na) 4 \nb) 5 \nc) 6 \nd) 7 \ne) 8\n"},
    {"b": "What is the second letter of the alphabet?\na) c \nb) b \nc) a \nd) e \ne) Not this one\n"},
    {'50': "Enter 50:\n"},
    {"Ryan": "What is the first name of the student who made this quiz?\n"},
    {"Ryan": "What is the first name of the student who made this quiz?\n"},
]
score = 0


def question_parser(question):
    '''Takes questions 
    instatiated above to ask user a question, 
    tell them if they are correct, 
    and store the user's score'''

    # takes question prompt from respective dict
    prompt = list(question.values()) 
    prompt = input(prompt.pop())
    print(prompt)

    # takes correct answer from respective dict
    answer = list(question.keys())
    answer = answer.pop()

    # if the user answered correctly
    if prompt.lower() == answer.lower():
        global score
        score += 1
        print(f"{answer} is the correct answer! Your score is: {score}\n")
    else:
        print(f"{prompt} is the incorrect answer! Your score is still {score}\n")


for question in questions:
    question_parser(question)

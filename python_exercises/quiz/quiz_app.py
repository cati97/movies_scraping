"""
[x] get each line of questions.txt - readlines() and separate questions and answers using split("=")
[x] in for loop ask each question to the user and ask for answer
[x] check if the answer (user input) is the same as extracted answer from questions.txt
[x] create a variable to score user's current result
[x] if it is the same add one point to the score
[x] after the loop save the score into result in format "Your score is 2/3"

"""

questions_file = open("questions.txt", "r")
questions_and_answers = [line.strip() for line in questions_file.readlines()]  # ["1+1=2"]
questions_and_answers_separately = [element.split("=") for element in questions_and_answers]
# [['1+1', '2'], ['2+2', '4'], ['7-4', '3']] the first element of each list is

questions = []
answers = []

for element in questions_and_answers_separately:  # first ['1+1', '2']
    questions.append(element[0])
    answers.append(element[1])


print(questions)
print(answers)

score = 0

for i in range(len(questions)):
    answer = input(f"{questions[i]} = ")
    if answer == answers[i]:
        print("Correct")
        score += 1
    else:
        print("Wrong")

result_file = open("result.txt", "w")
result_file.write(f"You score is: {score}/{len(questions)}")

result_file.close()

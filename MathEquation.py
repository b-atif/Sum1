# python 3.12.1

import random

def generate_equation():
    num_1 = random.randint(1, 9)  # Generate a random integer between 1 and 9 for the first number
    answer = random.randint(10,20) # Generate a random integer between 10 and 20 for what the eqn is equivalent to
    X = answer/num_1
    return num_1, X, answer, 

score = 0

# Generates a random equation five times
for _ in range(5):
    num_1, X, answer = generate_equation()
    message = "Solve the equation " + str(num_1) + " * " + '𝑥 ' + ' = ' + str(answer)
    print(message)
    user_answer = float(input("Your answer for X (1 dp if required) : "))
    user_answer = round(user_answer, 1) 
    X = round(X,1) # Ensures input can handle to 1 decimal place

    if user_answer == X: # Compares if users answer is equal to X
        print("Correct!")
        score += 1 # Adds up the score
    else:
        wrong_answer_message = "Wrong. The correct answer was: " + str(X)
        print(wrong_answer_message)

total_score = "Your score is: " + str(score) + " out of 5"
print(total_score)

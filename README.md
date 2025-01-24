# Sum1

# Introduction

This is a simple algebraic math equation game designed to hep users practice their algebra. The game presents the user to a random equation for which they are tasked to solve for the value '𝑥'. They are presented with 5 random equations to solve and then receive a total score out of 5 for however many were correct.

## User Guide

# Welcome to the Math Algebraic Equation game!
This game is a fun way to practice your algebra. You will see a random equation displayed on the screen, and your goal is to solve for '𝑥' and enter the corect number (to 1 decimal place if required). You will receive your score after you have attemempted the 5 equations!

Features:
- Randomly generated math equation to solve
- Immediate feedback on whether your answer is correct for each

What you'll need:
- A python environment installed in your computer
- Access to a terminal/command prompt

How to play:

1. Run the game in your terminal
2. Solve for the equation displayed on your screen
3. Enter your value for 𝑥
4. Try to get all 5 correct!

Example Gameplay:

<img width="683" alt="math eqn" src="https://github.com/user-attachments/assets/6e2e497c-3393-4cd9-a7cb-ac5d2a587346" />


## Technical Documentation

To clone this repository:

```bash
git clone https://github.com/b-atif/Sum1.git
```

# Program summary

This program generates a random equation in Python using the python library: random. The user will input a value for X, program checks if it's correct and once program is over it output's the total result.

# Logic of code

The way the input is handled is using the input() function where the user will enter a number for X. If the input is a decimal number, the round() function allows the input to be a value that's given to one decimal place. It also means that if the correct input is a whole number, the user will not have to convert that number into decimal. This number is converted into a float using float() to ensure the program can handle any decimal values that are input.

The logic for determining the value for X is through dividing the value the equation is equal to (the answer) by the first number in the equation in the equation. Using the 'If' condition statement, if the input value is the same as 'X', the score will add up and print 'Correct!', and using 'else' statement the if the input value is not the same as X , it will print the answer is wrong along with what the correct answer was. Both these messages are printed using the print() function.


# Running the code locally

To run tests locally, this will be performed on a computer rather than a server. The steps below gives a guide on how to do this:
- Open a terminal and run the code for the cloned repository mentioned above
- Install dependencies using the code ``` pip install -r requirements.txt ``` (please not this is only for requirements.txt files)
- Ensuring you have Visual Studio Code installed, open the project
- To run the code execute the code: ``` python script.py ``` OR you can simply use the 'Run' or play button in VS code

# How to Run Tests Locally

-To run tests locally, there would need to be a testing framework such as unittest or pytest
This can be installed using: ``` pip install pytest  ```
-Locate your test file and run it using the terminal in VS code: ```  pytest  ```
- Once run, the terminal will display which tests have passed and which have failed (adjustments can be made to the ones that have failed and then rerun)
- Now that the tests have passed this can be pushed to Github

Test Driven Development (TDD) can also be used where you write enough code for the tests to pass and if there is no output when run, all tests pass.

# Code Maintenance

Maintaining code is very important for making code understandable for yourself and those you work with. Here are some ways to maintain the code:

- Adding comments using the hash symbol: # (for Python) - used to describe what that specific code is doing etc.
- Naming conventions in a way that is relevant to the program. In this case I have used num_1, answer, X and user_answer as my variables that are relevant to an algebraic math equation
- I have used Indentation to make the code neater and easier for a programmer to link parts of the code


# Explanation of code

<img width="96" alt="image" src="https://github.com/user-attachments/assets/5d2bb1d1-fe17-445b-bcc8-0526915930f1" />

This is importing the 'random' library so we can generate random numbers for the game.

<img width="511" alt="image" src="https://github.com/user-attachments/assets/43637374-5cc0-4a02-ae32-157c9222ff71" />

Here, we define a function that is reusable and runs the tasks specific to what it has been defined by. The num_1 variable is the firt number in the equation and the answer variable is what the equation is equivalent to that can be used to find out the 'X' variable. The X will always be the 'answer' divided by num_1.

<img width="437" alt="image" src="https://github.com/user-attachments/assets/3a014c9d-fe30-42e4-9470-8f38d54fe3af" />

The variable 'score' is assigned a value of 0 because before the game starts the value will have to be 0 in order to add up as the game plays.
A for loop is now started to iterate the process of generating an equation.
range(5) suggests there will be an equation generated five times.
The generate_equation() is reused here to ensure that each time num1, X and answer are returned. 
'message' is another variable used to display what the equation to solve is for the user to see (using the print() operator)
Interactivity begins with the user_answer variable where the input function allows the user to put in the answer. Here, we have used a float() to ensure the program can handle decimal values.
round() is used to ensure the user input and 'X' only allows answers to one decimal place.


<img width="365" alt="image" src="https://github.com/user-attachments/assets/d16b2328-88cf-447f-9e24-6d43724e0818" />

The if statement is used to set conditions to compare if the user's answer is equal to the value of 'X' and will then 'print' the word 'Correct'. We can now also see the score will add the current value by 1 incrementally using '+= 1'
The else handles the incorrect answers using the 'wrong_answer_message' variable that prints: "Wrong. The correct answer was: " + str(X)". The 

<img width="314" alt="image" src="https://github.com/user-attachments/assets/740e5bc7-8a86-4ee8-82a5-47b1656d181b" />

A final variable is assigned what the user's final score is which is displayed using print()



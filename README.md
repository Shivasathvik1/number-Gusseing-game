<h1 align ="center"> Number Guessing Game </h1>

A simple command-line number guessing game built with Python. The computer picks a secret number between 1 and 50, and you have 10 attempts to guess it.

## How to Play
1.	Run the script using Python
2.	Enter a number between 1 and 50 when prompted
3.	The game tells you if your guess is too high or too low
4.	Keep guessing until you find the number or run out of attempts

## Rules
5.	You have 10 attempts to guess the correct number
6.	The secret number is always between 1 and 50
7.	If you enter a number outside 1–50, it counts as an invalid input and does not use up an attempt
8.	If you guess correctly, you win
9.	If you use all 10 attempts without guessing correctly, the game reveals the number and ends

## Requirements
Python 3.x — No external libraries needed (only uses the built-in random module)

## How to Run
python number_guessing.py

## Example
Attempt 1 Choose your number from 1-50: 25
Your guess is wrong! try Higher
 
Attempt 2 Choose your number from 1-50: 38
Your guess is wrong! try lower
 
Attempt 3 Choose your number from 1-50: 31
Congrats You won The Game 🥳🥳

# Code Overview
Code	Description
random.randint(1, 50)	Generates the secret number between 1 and 50
while True	Keeps the game loop running until a break is hit
continue	Skips invalid inputs without counting as an attempt
break	Stops the game when the player wins or runs out of attempts
Attempt += 1	Tracks how many valid guesses have been made

Author
Built as a beginner Python project to practice loops, conditionals, and user input.

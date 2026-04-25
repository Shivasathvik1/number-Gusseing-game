import random
print("""
                          Welcome to number guessing.
                    You have 10 chances to guess the number.
    if You not able to Guess the number in Ten attempts you are out of the game """)
secret_number = random.randint(1,50) #Genarating a random number using randint from function random
Attempt = 1 # created a variable attempt and stored 1
while True:
    user_input=int(input(f"Attempt {Attempt} Choose your number from 1-50: ")) # asking user to give an integer input
    if user_input > 50 or user_input < 1: # if user choose a number less thn 0 and greater than 50 it will give you invalid input 
        print("invalid input")
        continue
    elif secret_number == user_input: #here it will check secret number and usper input both are same or not if yes it will print you are win
        print("Congracts You won The Game 🥳🥳")
        break
    elif secret_number < user_input: # here it will check the user input is less than secret number or not if yes it will display try low number
        print("Your guess is worng! try lower")
    elif secret_number > user_input: # here it will check the user input is greater than secret number or not if yes it will display try low number
        print("Your guess is worng! try Higher")
    Attempt +=1 # after every attempt value in attempt will increase by 1 and store in attempt 
    if Attempt >10:# here it will check the attempt is greater than 10 or not if yes it will display gave over message
        print(f'the Number was {secret_number} ,GAME OVER!😩')
        break
    
    

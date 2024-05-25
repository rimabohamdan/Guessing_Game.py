import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    user_guess = None
    
    print("welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")
    
    while user_guess != number_to_guess :
        user_guess = int(input("Enter your guess: "))
        if user_guess < number_to_guess :
            print("Your guess is too low. Try again!")
        elif user_guess > number_to_guess :
            print("Your guess is too high. Try again!")
        else:
            print(f"Congratulations! You've guessed the correct number: {number_to_guess}")
            
if __name__ == "__main__" :
    guessing_game()
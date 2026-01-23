# Guess the number challenge
# print no of guesses left. Number of guesses took to finish games
# If not guessed print game over

n = 15
NumberofGuesses = 8
guesses_taken = 0

while NumberofGuesses > 0:
    user_input = int(input("Guess the number: "))
    guesses_taken += 1
    NumberofGuesses -= 1

    if n>user_input:
        print("Tager number is greater than guessed number")  
    elif n<user_input:
        print("Tager number is smaller than guessed number")  
    else:
        print("You Guessed the number correctly")
        print(f"You guessed in {guesses_taken} chances.")
        break
    print(f"Number of Guesses left : {NumberofGuesses}")

else:
    print("Game Over")
    print(f"The correct number was {n}")


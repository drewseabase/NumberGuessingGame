import random

low = int(input("Enter a low number: "))
high = int(input("Enter a high number: "))
iterations = 0
guesses = 0
has_won = False
random_num = random.randint(low, high)

print("Lets play a game!")
print("You chose a range of numbers, and I picked a random number between that range")
print("You get a certain amount of guesses to guess that number")
print(f'Your range is from {low} to {high}!')

while low <= high:
    iterations+=1
    mid = low + (high - low) // 2
    if mid == random:
        break
    elif mid < random_num:
        low = mid + 1
    else:
        high = mid - 1

print(f'You have {iterations + 1} chances to guess the correct number!')

while guesses != iterations + 1:
    guess_num = int(input("Guess the number: "))
    guesses+=1



    if guess_num == random_num:
        print(f'Guess {guesses}: {guess_num} → Correct! ')
        has_won = True
        break

    elif guess_num < random_num:
        print(f'Guess {guesses}: {guess_num} → Too low')
    else:
        print(f'Guess {guesses}: {guess_num} → Too high')


if guesses == iterations + 1 and has_won == False:
    print("Sorry, you failed to guess the correct number!")
    print(f'The correct number was {random_num}')




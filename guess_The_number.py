import random
rand_number = random.randint(1,5)
# print(rand_number)
guess_number = True
guesses = 0

while guess_number!=rand_number:
    guess_number = int(input("Enter the guess number: "))
    guesses +=1
    if guess_number==rand_number:
        print("you guess it right!!")
    else:
        if guess_number>rand_number:
            print("you guess it wrong!..Enter smaller number")
        else:
            print("you guess it wrong!..Enter larger number")
print(f"you guess the number in {guesses} guesses")

with open("highest.txt","r") as f:
    hiscore = int(f.read())

if guesses < hiscore:

    with open("highest.txt","w") as f:
        print("you just broken the high score!!!")
        f.write(str(guesses))
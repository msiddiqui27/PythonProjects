import random  # module to import

rangeTop = input("Type a number: ")

if rangeTop.isdigit():  # if rangetop is a number, it will reutrn as true and then we will convert it to int
    rangeTop = int(rangeTop)
    if (rangeTop <= 0):
        print("please type a number greater than 0: ")
        quit()
else:
    print("please input a number: ")
    quit()
randomN = (random.randint(0, rangeTop))
# follows patter: random.randrange(start,stop) of random numbers being generated
incorrect = 0
guesses = 0
while True:
    # user types in a number, it comes in as a string. If the input is a number, it will convert it to an int
    userGuess = input("Make a guess: ")
    guesses += 1
    if userGuess.isdigit():
        userGuess = int(userGuess)
    else:  # if the input isn't a number, then it will ask gto try again, causing the loop to reiterate
        print("Please input  a number instead: ")
        continue

    if (userGuess == randomN):
        print("Correct! :)")
        if guesses == 1:
            print("You got it in 1 guess!")
        else:
            print("You got it in", guesses, "guesses")
    elif userGuess > randomN:
        print("Your guess is above the number!")
    else:
        print("Your guess is below the number!")

    if userGuess != randomN:
        print("Incorrect!")
        incorrect += 1
        if incorrect == 5:
            print("You have run out of guesses. Play again!")
            break

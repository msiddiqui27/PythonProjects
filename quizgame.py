print("Welcome to computer quiz!")
# like scanner. asks user to put input into console
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()  # immediatley termiantes program if what the user typed in isn't equal to "yes"

print("Let's start :)")
score = 0

answer1 = input("What does CPU stand for? ").lower()

if answer1 == "central processing unit":
    print('Correct!')
    score += 1

else:
    print("Incorrect :(")

answer2 = input("What does GPU stand for? ").lower()

if answer2 == "graphics processing unit":
    print('Correct!')
    score += 1

else:
    print("Incorrect :(")

answer3 = input("What does RAM stand for? ").lower()

if answer3 == "random access memory":
    print('Correct!')
    score += 1

else:
    print("Incorrect :(")
answer4 = input("What does PSU stand for? ").lower()

if answer4 == "power supply unit":
    print('Correct!')
    score += 1

else:
    print("Incorrect :(")

# score is an int, so converting the number to a string will print the whole string
print("You got " + str(score)+" questions correct!")
print("...which is " + str((score/4)*100)+"%")

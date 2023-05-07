print("Welcome to my Quiz!")
isplaying = input("Are you interested to play quiz? : ")
if (isplaying.lower() != 'yes'):
    quit()
else:
    print("Thanks for choosing to play! Let's play! :) ")

score = 0

answer = input("What does CPU Stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer = input("What does GPU Stand for? ")
if answer.lower() == "graphic processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer = input("What does RAM Stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer = input("What does PSU Stand for? ")
if answer.lower() == "power supply unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + " %.")

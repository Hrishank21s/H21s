print("Hey There, This is a quiz game")
print('')#for line space
playing=input('Do you want to play?(Yes/No): ').lower()
if playing == "no":
    print("Please feel free to play again anytime!")
    quit()
elif playing == 'yes':
    print("Lets Begin!")
else:
    print('Invalid Command')
    quit()
score=0
answer= input("What is CPU stands for?: ").lower()
#"in [], is use for input in list"
if answer  in ["central processing unit", "hh"]:
    score += 1
    print("Correct Answer!")
else:
    print("Incorrect :-)")
#testing start
answer = input("What do you use to move the cursor on the computer screen?: ").lower()
if answer == "mouse":
    score += 1
    print("Correct Answer!")
else:
    print("Incorrect :-(")
answer = input("Which button do you press to turn on a computer?: ").lower()
if answer == "power":
    score += 1
    print("Correct Answer!")
else:
    print("Incorrect :-(")
answer = input("What do you call a small program that performs a specific task on a computer?: ").lower()
if answer == "app":
    score += 1
    print("Correct Answer!")
else:
    print("Incorrect :-(")
answer = input("What is the term for a picture or symbol that represents a program or file on the computer screen?: ").lower()
if answer == "icon":
    score += 1
    print("Correct Answer!")
else:
    print("Incorrect :-(")
answer = input("Which device do you use to type on a computer?: ").lower()
if answer == "keyboard":
    score += 1
    print("Correct Answer!")
else:
    print("Incorrect :-(")
answer = input("What do you call the process of shutting down a computer?: ").lower()
if answer == "shutdown":
    score += 1
    print("Correct Answer!")
else:
    print("Incorrect :-(")
#Testing stop
answer= input("What is GPU stands for?: ").lower()
if answer.lower()== "graphics processing unit":
    score += 1
    print("Correct Answer!")
else:
    print("Incorrect :-)")
answer = input("What is RAM stands for?: ").lower()
if answer.lower() == "random access memory":
    score += 1
    print("Correct Answer!")
else:
    print("Incorrect :-)")
answer = input("What is 'MB' stands for?: ").lower()
if answer.lower() == "mega byte":
    score += 1
    print("Correct Answer!")
else:
    print("Incorrect :-)")
answer = input("What do display used to operate computer called?: ").lower()
if answer.lower() == "monitor":
    score += 1
    print("Correct Answer!")
else:
    print("Incorrect :-)")
print("Quiz complet, Thanks for playing")
print("You Got "+ str(score)+ " Question Correct Out of 12!")
print("You Got "+ str((score/11)*100)+ "%")
replay= input("Do you want to play again?(Yes/No): ").lower()
if replay == "yes":
    print("Lets go again!")
else:
    print("Thanks for playing!")
    print("testing guthub do adding this text so thai I am able to chech it on github, Thanks!")
    quit()




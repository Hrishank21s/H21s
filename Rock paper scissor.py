import random

user_wins=0
computer_wins=0
scissor ="scissor's"
options=["Rock","Paper","scissor"]
while True:
    user_input=input("Type Rock,Paper,scissor's or 'Q' to quit: ").lower()
    if user_input == 'q':
        print("thankyou, come again anytime!")
        break
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]

    print("computr Picked ", computer_pick)
    if user_input== "rock" and computer_pick=="scissor":
        print('You win')
        user_wins += 1
    elif user_input== "paper" and computer_pick=="rock":
        print('You win')
        user_wins += 1
    elif user_input== "scissor" and computer_pick=="paper":
        print('You win')
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1


print("you won ", user_wins,"times")
print("computer won ", computer_wins, 'times')


print('goodbye')



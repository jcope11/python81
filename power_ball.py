#! /usr/bin/python3
# Powerball simulator
# White balls numbered 1 to 69, pick 5
# Red balls numbered 1 to 26, pick one

from random import randint

def check_duplicates():
    len_of_list = len(ticket)
    len_of_set = len(set(ticket))
    if len_of_list == len_of_set:
        return True

def check_range():
    if pick > 0 and pick < 70:
        return True


white_balls = []
red_balls = []
white_pick = []
red_pick = ""
ticket = []

for i in range(1, 70):
    white_pick.append(i)
for i in range(1, 27):
    red_balls.append(i)
print("POWER BALL")
print("Select 5 white balls numbered from 1 to 69")

# Select 5 white balls from 1 to 69
for i in range(1, 6):
    while True:
        pick = input("White Ball #"+ str(i) +": ")
        if pick.isdigit():
            pick = int(pick)
            if check_range():
                ticket.append(int(pick))
                if check_duplicates():
                    break
                else:
                    print("You already chose that number. Pick another.")
                    ticket.pop()
            else:
                print("Please enter a number from 1 to 69.")
        else:
            print("Please enter numbers only.")

print(ticket)
# Select 1 red ball from 1 to 26
print("Select 1 red ball numbered from 1 to 26")
while True:
    pick = input("Red Ball: ")
    if pick.isdigit():
        pick = int(pick)
        if pick > 0 and pick < 27:
            red_pick = pick
            break
        else:
            print("Please enter a number from 1 to 26.")
    else:
        print("Please enter numbers only.")

print("\nYour Powerball Lottery Ticket:")
ticket.sort()
for i in range(len(ticket)):
    print(ticket[i], end="  ")
print('\033[91m',red_pick,'\033[0m')

odds = 69 * 68 * 67 * 66 * 65 * 26
print(f"Your odds of winning are {odds:,} to 1")

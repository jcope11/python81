#! /usr/bin/python3
# Powerball simulator
# White balls numbered 1 to 69, pick 5
# Red balls numbered 1 to 26, pick one

import time
import random
from random import randint

# initialize variables
white_balls = []
red_balls = []
white_pick = []
red_pick = ""
ticket = []
color_red = "\033[91m"
color_white = "\033[0m"
color_yellow = "\033[93m"
global red_winning_number
global white_winning_numbers
# global str_red_winning_number


def range_check(pick):
    if pick > 0 and pick < 70:
        return True


def duplicate_check():
    len_of_list = len(ticket)
    len_of_set = len(set(ticket))
    if len_of_list == len_of_set:
        return True


def spinning_cursor(spin):
    for j in range(spin):
        for cursor in '\\|/-':
            time.sleep(0.08)
            print(f"\b{cursor}", end="", flush=True)


def slowpick():
    """ Select white and red balls """
    # Select 5 white balls from 1 to 69
    global red_pick
    global ticket
    ticket = []  # reset ticket to null (needed for replays)
    print("Select 5 numbers from 1 to 69: ")
    for i in range(1, 6):
        while True:
            pick = input("White Ball #" + str(i) + ": ")
            if pick.isdigit():  # check that the input string is a digit
                pick = int(pick)
                if range_check(pick):  # check that the input digit is within 1 to 69 inclusive
                    ticket.append(int(pick))
                    if duplicate_check():
                        break
                    else:
                        print("You already chose that number. Pick another.")
                        ticket.pop()
                else:
                    print("Please enter a number from 1 to 69.")
            else:
                print("Please enter numbers only.")

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
    # return


def quickpick(qp_ticket_amt):
    qp_ticket_amt = int(qp_ticket_amt)
    global qp_ticket
    qp_ticket = []


def purchase_tickets():
    # Purchase tickets
    print("--- PLAY POWER BALL ---")
    print(f"Your odds of winning are 292,201,338 to 1\n")
    print("Select 5 white balls numbered from 1 to 69")
    print("Select 1 red ball numbered from 1 to 26")
    qp = input("Would you like: \n(1) QuickPick Ticket \n(2) Choose your own numbers : \n")

    # validate for 1 or 2
    while True:
        if qp == '1' or qp == '2':  # validate 1 or 2, otherwise get new input
            break
        else:
            qp = input("Please select: \n(1) QuickPick Ticket \n(2) Choose your own numbers: \n")
    # Take action on 1 or 2
    if qp == '1':  # QuickPick selected
        qp_ticket_amt = input("How many tickets: ")
        quickpick(qp_ticket_amt)
    elif qp == '2':  # user selects his own number
        slowpick()

def draw_balls():
    global white_winning_numbers
    print("Drawing lottery balls now:")
    white_winning_numbers = []

    # Draw 5 white balls
    for i in range(5):
        ball_drop = random.choice(white_balls)  # choose white ball at random
        white_winning_numbers.append(ball_drop)  # add to list of white balls selected
        white_balls.remove(ball_drop)  # remove the number so it's not selected again
        str_ball_drop = str(ball_drop)  # convert value to a string so we can right justify formatting
        print(f"\b{str_ball_drop.rjust(2)}    ", end="")  # print selected balls with a slight delay
        spinning_cursor(4)

    # Draw 1 red ball
    global red_winning_number
    global str_red_winning_number
    red_winning_number = random.choice(red_balls)
    str_red_winning_number = str(red_winning_number)
    print(f"\b{color_red}{str_red_winning_number.rjust(2)}{color_white}\n")


def print_ticket():
    print("Your Powerball Lottery Ticket:")
    # Print Lottery ticket
    ticket.sort()
    for i in range(len(ticket)):
        print(str(ticket[i]).rjust(2), end="   ")
        red_pick_string = str(red_pick)  # convert to string for right justify method
    print(f"{color_red}{red_pick_string.rjust(2)}{color_white}")

def print_winning_numbers():
    # Print  winning numbers
    print("The winning Powerball numbers are:")
    white_winning_numbers.sort()
    for i in range(5):
        print(f"{str(white_winning_numbers[i]).rjust(2)}   ", end="")  # print 5 white numbers
    print(f" \b{color_red}{str_red_winning_number.rjust(2)}{color_white}")  # print 1 red number


def find_matches():
    # Find white matches
    match_white = set(white_winning_numbers) & set(ticket) # find intersection of two sets
    matches_white = len(match_white)  # find length of the set. If zero, no matches
    print(f"You matched {color_yellow}{matches_white}{color_white} of the white numbers!")

    # Find red matches
    if red_pick == red_winning_number:
        matches_red = 1
        print(f"You matched the red Powerball number!")
    else:
        matches_red = 0
        print(f"You matched {color_yellow}0{color_white} of the red numbers!")
    # print you suck
    if matches_white == 0 and matches_red == 0:
        print("\nYou matched no numbers.\n"
              "You really suck at playing the lottery!")


# Create a list of white and red balls
for i in range(1, 70):
    white_balls.append(i)
for i in range(1, 27):
    red_balls.append(i)

def run():
    purchase_tickets()
    print_ticket()
    draw_balls()
    print_winning_numbers()
    print_ticket()
    find_matches()


# Run the program
run()


# Play again?
while True:
    again = input("\nWould you like to play again (y/n): ")
    if again == "y":
        run()
    else:
        print("\nThank you for donating your money to the government, sucker!")
        exit()

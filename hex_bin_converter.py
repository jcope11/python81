#! /usr/bin/python3
# Decimal, Hex, and Binary Number Converter

from termcolor import colored  # Must import termcolor module and install in same directory

print("Decimal - Hex - Binary Converter\nby Joe Copeland\n")

while True:
    response = input('Enter the starting number (e.g. 0): ')
    if response == "":
        response = '0'  # Start at 0 by default.
        break
    if response.isdecimal():
        break
    print('Please enter a number greater than or equal to 0.')
start = int(response)

while True:
    response = input('Enter how many numbers to display (ex. 1000): ')
    if response == '':
        response = '1000'  # Display 1000 numbers by default
        break
    if response.isdecimal():
        break
    print("Please enter a number.")
amount = int(response)

for number in range(start, start + amount):  # Main program loop.
    # Convert to hex/binary and remove the prefix 0b and 0x
    hexNumber = hex(number)[2:].upper()
    binNumber = bin(number)[2:]

# Print table in color with colored function.  eg colored("text", 'green')
    print('Dec:', colored(number,'green'),'   Hex:', colored(hexNumber,'green'), '   Bin:', colored(binNumber, 'green'))

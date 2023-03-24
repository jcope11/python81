#! /usr/bin/python3
# Decimal, Hex, and Binary Number Converter

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

# Print colorful table using ANSI color codes
color_white = '\033[0m'
color_green = '\033[92m'
color_yellow = '\033[93m'
color_blue = '\033[94m'

for number in range(start, start + amount):  # Main program loop.
    # Convert to hex/binary and remove the prefix 0b and 0x
    hexNumber = str(hex(number)[2:].upper())
    binNumber = str(bin(number)[2:])
    number = str(number)
    print('Dec:', color_green + number + color_white, '   Hex:', color_yellow + hexNumber + color_white, '   Bin:', color_blue + binNumber + color_white)

import sys, time, sevseg

# my_number = sevseg.getSevSegStr(11, 3)
# print(my_number)

# (!) Change this to any number of seconds:
secondsLeft = int(input("How many seconds: "))
# secs = input("How many seconds: ")
# secondsLeft = int(secs)

try:
    while True:  # Main program look
        # print('\n' * 25)

        # get hours, minutes, and seconds, remaining
        hours = str(secondsLeft // 3600)
        minutes = str((secondsLeft % 3600) // 60)
        seconds = str(secondsLeft % 60)

        # get the digits from the seven segment module
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()
        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()
        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Display the digits
        print(hTopRow    + '   ' + mTopRow    + '   ' + sTopRow)
        print(hMiddleRow + ' * ' + mMiddleRow + ' * ' + sMiddleRow)
        print(hBottomRow + ' * ' + mBottomRow + ' * ' + sBottomRow)

        if secondsLeft == 0:
            print()
            print('   * * * * BOOM * * * *')
            break
        # print()
        # print('Press Ctrl-C to quit.')

        time.sleep(1)
        secondsLeft -= 1
except:
    sys.exit()



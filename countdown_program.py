#Countdown timer code

import time
def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)
    print("Blast off!")

print("How many seconds to count down? Enter an integer:")
seconds = input()
while not seconds.isdigit():
    print("That wasn't and integer! Enter an integer:")
    seconds = input()
seconds = int(seconds)
countdown(seconds)
    

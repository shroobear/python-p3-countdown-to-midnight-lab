import time
# your code goes here!
def countdown(int):
    while int > 0:
        print(f'{int} SECOND(S)!')
        int -= 1
    if int == 0:
        print("HAPPY NEW YEAR!")

def countdown_with_sleep(int):
    while int > 0:
        print(f'{int} SECOND(S)!')
        int -= 1
        time.sleep(1)
    if int == 0:
        print("HAPPY NEW YEAR!")

countdown_with_sleep(15)
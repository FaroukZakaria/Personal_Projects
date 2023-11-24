import time
import random
"""
    A small game that tests reflex.
    As soon as "GO" is printed. player must hit spacebar immediately.
    if he hit before time, he wins, otherwise loses.
"""
def main():
    while True:
        print("Ready?\n...")
        lst = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
        inp = None
        go_time = random.shuffle(lst)
        time.sleep(lst[0])
        print("GO!!!")
        timer = time.time()
        inp = input("Enter when 'GO' appears!")
        while inp == None:
            continue
        end = time.time()
        result = end - timer
        print(f"You took {result:.2f} seconds\n---")
        time.sleep(0.2)
        breaker = input("Play again?")
        if breaker == 'y':
            continue
        else:
            break
main()
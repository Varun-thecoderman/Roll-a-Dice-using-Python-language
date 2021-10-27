import random
import time

min_val = 1
max_val = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling The Dice...\n")
    time.sleep(.9)
    print("Dice face value is:")
    
    print(random.randint(min_val, max_val),'\n')
    time.sleep(.7)
    
    roll_again = input("Roll the Dice Again?")

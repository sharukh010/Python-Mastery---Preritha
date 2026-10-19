import random 
import time , os 

value = random.randint(1,2)
print("Coin is spinning...")
time.sleep(4)
os.system("cls")
if value == 1: 
    print("Heads")
else: 
    print("Tails")


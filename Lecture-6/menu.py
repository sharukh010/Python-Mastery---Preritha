BURGER=1
FRIES=2
CHIPS=3 

COFFEE=1
JUICE=2
TEA=3

bevarages = """options: 
1. Burger
2. Fries
3. Chips"""

drinks = """options: 
1. Coffee
2. Juice
3. Tea"""

print(bevarages)
choice1 = int(input("Enter your choice (1-3): "))
print(drinks)
choice2 = int(input("Enter your choice (1-3): "))

match choice1: 
    case 1: 
        print("Burger")
    case 2: 
        print("Fries")
    case 3: 
        print("Chips")

match choice2: 
    case 1: 
        print("Coffee")
    case 2: 
        print("Juice")
    case 3: 
        print("Tea")

    
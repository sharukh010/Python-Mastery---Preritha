"""
day number (1-7)
you need to print if it is monday - sunday 
1. monday 
2. tuesday 
...
7. Sunday 
"""
day_number = int(input("Day Number (1-7): "))
match day_number: 
    case 1: # day_number == 1 
        print("Monday")
    case 2: 
        print("Tuesday")
    case 3: 
        print("Wednesday")
    case 4: 
        print("Thursday")
    case 5: 
        print("Friday")
    case 6: 
        print("Saturday")
    case 7: 
        print("Sunday")
    case _ : # else in if else (default case)
        print("Invalid day number.Try again")
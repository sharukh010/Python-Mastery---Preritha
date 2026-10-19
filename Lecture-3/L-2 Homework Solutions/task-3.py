age = int(input("Enter you're age: "))
if age >= 6 and age <= 17: 
    print("Junior card")
elif age>=18 and age <= 59: 
    print("Adult card")
else: 
    print("Visit the help desk")
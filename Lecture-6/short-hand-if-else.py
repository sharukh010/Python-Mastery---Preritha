age = int(input("Enter your age: "))
verdict = ""
if age >= 18: 
    verdict = "Adult"
else: 
    verdict = "Minor"

verdict = "Adult" if age >= 18 else "Minor" 
          # value-1                 # value-2 

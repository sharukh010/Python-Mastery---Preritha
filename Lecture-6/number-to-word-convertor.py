"""
our goal is to convert 123 -> "one two three" 
before doing that we need to convert single digit from number to word 
like 
1 -> one 
2 -> two 
"""
# digit = int(input("Enter a digit (0-9): "))
number = input("Enter a number: ")
word = ""
for digit in number: 
    digit = int(digit)
    match digit: 
        case 1: 
            word += "one"
        case 2: 
            word += "two"
        case 3: 
            word += "three"
        case 4:
            word += "four"
        case 5: 
            word += "five"
        case 6: 
            word += "six"
        case 7: 
            word += "seven"
        case 8: 
            word += "eight"
        case 9: 
            word += "nine"
        case 0: 
            word += "zero"
    word += " "
print(word.title())
"""
our goal is to get "one two three" -> 123 
first we need to work on getting "one" -> 1 
"two" -> 2 
"""
print("""Examples: 
1. 123 - one two three 
2. 103 - one zero three
-> every word should be seperated by space 
""")
words = input("Enter number in words: ").lower().split()
number = ""
for word in words: 
    match word: 
        case "one": 
            number += "1"
        case "two": 
            number += "2"
        case "three": 
            number += "3"
        case "four": 
            number += "4"
        case "five": 
            number += "5"
        case "six": 
            number += "6"
        case "seven": 
            number += "7"
        case "eight": 
            number += "8"
        case "nine": 
            number += "9"
        case "zero": 
            number += "0"
print(number)
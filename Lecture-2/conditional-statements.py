"""
if condition: <- starting of block of code 
    line-1
    line-2 
line-3 - this line doesn't come under conditional statement 
you will only execute line-1,2 if the condition is true other wise you will not 
execute it 
"""
# num = 21 
# if num%2 == 0:
#     print("Even number")
# else: # this will execute when the above condition is false 
#     print("Odd number")


# else is dependent on if you cannot write else without if 
# but you can write if without else 
# if num%2 != 0: 
#     print("Odd number")
# for mutually exclusive conditions it is better to use elif or else 

light = input("Enter a colour (red/yellow/green): ")
if light == "red": 
    print("STOP")
elif light == "yellow": 
    print("WAIT")
elif light == "green": 
    print("GO")
else: 
    print("Invalid traffic light colour")
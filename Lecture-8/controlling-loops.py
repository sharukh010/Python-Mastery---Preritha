"""
break -> stop the loop 
continue -> skip the iteration 
"""

# for num in range(1,11): 
#     if num %2 == 1: 
#         continue # skipping # move to line number 7 
#         # print('hello') # not allowed 
#     # print("hello")
#     print(num) # logic for printing 

for num in range(1,11): 
    if num == 7: 
        break # it moves to line number 17 
    print(num)

"""
n = 5
total = 0  
(1,2,3,4,5)
num = 1 
total = 0 + 1 = 1 
num = 2 
total = 1 + 2 = 3 
.. 

"""

n = int(input("Enter the N value: "))
total = 0 
for num in range(1,n+1): 
    total += num 

print(total)
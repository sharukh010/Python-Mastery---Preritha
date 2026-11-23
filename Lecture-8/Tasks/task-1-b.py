start = int(input("Enter starting point: "))
end = int(input("Enter ending point: "))
stop = int(input("Enter stop point: "))

for num in range(start,end+1): 
    if num == stop: 
        break 
    print(num)
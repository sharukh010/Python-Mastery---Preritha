start = int(input("Enter starting point: ")) 
end = int(input("Enter ending point: "))
skip = int(input("Enter skipping piont: "))

for num in range(start,end+1): 
    if num == skip: 
        continue # skip if number is equal to skip 
    print(num)
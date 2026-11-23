"""
for loop is used to go over a sequece of items 

index: it like position of item in a sequence 
- how many items you need to skip to reach a particular item 
p   r   e   r   i   t   h   a 
0   1   2   3   4   5   6   7 -> indexes
-8 -7  -6  -5  -4  -3  -2  -1 -> negative indexing 
when you go beyod 7 it will give out of index error
negative indexing tells the position of item from the last 
negative indexing starts from -1  

"""
name = "preritha"
# for c in name: 
#     print(c)
# print(name[8])
# print(name[1])

# print(name[-6])

# string slicing operation 
# [start:end:step]
# start,end,step -> optional 
# start = 0 
# end = length 
# step = 1 -> number of steps to take to get the next item in the sequence 
# print(name[3:8])
# print(name[-5:0])
# print(name[:8])
# print(name[0:])
# print(name[3:8:2])
# print(name[::3])
# print(name[-5:])
# print(name[-5]*2,name[-1]*2)

# range(10) -> 0 to 9 
# range(1,11) -> 1 to 10 
# range(1,11,2) ->1,3,5,7,9  

print(name[::-1]) # reverse the sequence 
# length = len(name)
# for i in range(length): 
#     print(name[i])
number_of_slices = int(input("Enter the number of slices: "))
number_of_friends = int(input("Enter the number of friends: "))
each_person_share = number_of_slices // number_of_friends
remaining_slices = number_of_slices % number_of_friends
print(f"Each friend gets {each_person_share} slices")
print(f"Slices left over: {remaining_slices}")
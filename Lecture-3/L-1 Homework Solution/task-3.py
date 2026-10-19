seconds = int(input("Enter the time (seconds): "))
hour = seconds // 3600 
remaining_second = seconds % 3600 # this will include minutes + seconds 
minute = remaining_second // 60 # this will remov the seconds part 
remaining_second  = remaining_second  % 60  # this will remove the minutes part 
print(f"{hour} Hours {minute} minutes {remaining_second } seconds")

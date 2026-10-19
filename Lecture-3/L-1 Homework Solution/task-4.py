distance = float(input("Enter the distance: "))
number_of_passengers = int(input("Enter the number of passengers: "))
fixed_fare = 40 
fare_per_km = 15 
total_fare = fixed_fare + (distance * fare_per_km ) 
per_person_share = total_fare / number_of_passengers 
print(f"Total fare: {total_fare}")
print(f"Each passenger pays: {per_person_share}") 

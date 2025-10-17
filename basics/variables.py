# Travel Budget Estimator Program
# Prompt: Create a simple Travel Budget Estimator program.
# Requirements: 
# Define variables for:
# 1. Destination name
# 2. Flight cost
# 3. Hotel cost per night
# 4. Number of nights
# 5. Daily food cost
# Calculate: Total cost for hotel stay, total food cost, and total trip cost.
# Print a summary

destination_name = input('Enter your destination name:')
flight_cost = float(input('Enter your flight cost:'))
hotel_cost_per_night =float(input('Enter your hotel cost per night:'))
number_of_nights = int(input('Enter number of nights you will stay:'))
daily_food_cost = float(input('Enter your daily food cost:'))
total_cost = flight_cost + hotel_cost_per_night * number_of_nights + number_of_nights * daily_food_cost
print(f'Travel Budget Estimator \n Destination is {destination_name} \n Flight cost is {flight_cost} \n Hotel cost per night is {hotel_cost_per_night} \n Number of nights is {number_of_nights} \n Daily food cost is {daily_food_cost} \n Total trip cost is {total_cost}')
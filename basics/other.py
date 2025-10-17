# Convert Km to Miles
km_amount = float(input('Enter the distance in killometer:'))
miles_amount = km_amount * 0.621371
print(f'{km_amount} in killometer is {miles_amount} in miles')

# Calculate the displacement
initial_velocity = int(input('What is the initial velocity?'))
final_velocity = int(input('What is the final velocity?'))
accelaration = int(input('What is the acceleration?'))
displacement = (final_velocity ** 2 - initial_velocity ** 2) / (2 * accelaration)
print(f'the total displacement {displacement}')


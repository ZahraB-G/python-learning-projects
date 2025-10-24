# Calculate the weekly weges for a worker with sepecific wage
# if he works over time he should earn 1.5 times of his regular wage.
def total_working_hours(hours):
    sum = 0
    for item in hours:
        sum += item
    return sum

def calculate_wage(total_hours, wage):
    if total_hours <= 40:
        return total_hours * wage
    else:
        return ((total_hours - 40)* 1.5*wage) + (40 * wage)

hours = list((input('Enter the hours that you worked this week: ').split(' ')))
hours_list = []
for item in hours:
    if item.isdigit and item != '':
        i = int(item)
        hours_list.append(i)
    
wage = float(input('Enter your hourly wage: '))
total_hours = total_working_hours(hours_list)
payment = calculate_wage(total_hours, wage)
print(f'Total wages is {payment}')



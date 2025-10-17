# Calculate the area of different geometric shapes
# Support for traingle, trapezoid, and circle

# Calculate the area of a triangle
height = int(input('Enter the height of the traingle:'))
base = int(input('Enter the base of the traingle:'))
area_triangle = 0.5 * base * height
print(f'The area of the traingle {area_triangle}')

# Calculate the area of a trapezoid
side_a = int(input('Enter the length of side a of the trapezoid:'))
side_b = int(input('Enter the length of side b of trapezoid:'))
height = int(input('Enter the height of trapezoid:'))
area_trapezoid = 0.5 * (side_a + side_b) * height
print(f'The area of trapezoid is {area_trapezoid}')

# Calculate the area of a circle
import math
radius = int(input('Enter the radius of the circle:'))
area_circle = math.pi * (radius**2)
print(f'The area of circle is {area_circle}')

# Calculate tje surface area of cuboid
length = int(input('Enter the length of cuboid: '))
breadth = int(input('Enter the breadth of cuboid: '))
height = int(input('Enter the height of cuboid: '))
area_cuboid = 2 * (length * breadth + length * height + breadth * height)
print(f'The aread of cuboid is {area_cuboid}')
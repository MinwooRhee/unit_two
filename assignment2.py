# Minwoo Rhee
# 9/21/18 11:12 AM
# assignment2
# program that draws two lines and tells the angle between them from the user input of two points

import math

import turtle

print("This program will ask you to enter the coordinates of two points in a xy plain.")

print("Then it will draw two lines, one connecting the origin and the first point,")

print("the other connecting the first point and the second point.")

print("It will also tell you the acute angle between the two lines in degrees.")

print("CAUTION : this program will function only when the two lines make an acute angle")

x_coordinate_first_point = input("Input the x coordinate of the first point, in arabic numbers: ")

y_coordinate_first_point = input("Input the y coordinate of the first point, in arabic numbers: ")

x_coordinate_second_point = input("Input the x coordinate of the second point, in arabic numbers: ")

y_coordinate_second_point = input("Input the y coordinate of the second point, in arabic numbers: ")

# float() is used because input() takes the input as a string
# slope = (y2 - y1) / (x2 - x1)

slope_first_line = (float(y_coordinate_first_point) - 0) / (float(x_coordinate_first_point) - 0)

slope_second_line = (float(y_coordinate_second_point) - float(y_coordinate_first_point)) \
                    / (float(x_coordinate_second_point) - float(x_coordinate_first_point))

# math.atan() gives the arctangent of the value.
# abs() gives the absolute value, which is useful when you have t*o subtract smaller variable from a bigger variable.
# acute angle in radians between two lines : |slope1 - slope2| / (1 + slope1 * slope2)

angle_in_radians = math.atan(abs(slope_first_line - slope_second_line)
                             / (1 + slope_first_line * slope_second_line))

angle_in_degrees = angle_in_radians * 180 / math.pi

turtle.speed(5)

turtle.goto(float(x_coordinate_first_point), float(y_coordinate_first_point))

turtle.write(abs(angle_in_degrees), move=False, align="left", font=("Arial", 16, "bold"))

turtle.goto(float(x_coordinate_second_point), float(y_coordinate_second_point))

turtle.exitonclick()

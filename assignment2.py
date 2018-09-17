import math

import turtle



x_coordinate_first_point = input("Input the x coordinate of the first point: ")

y_coordinate_first_point = input("Input the y coordinate of the first point: ")

x_coordinate_second_point = input("Input the x coordinate of the second point: ")

y_coordinate_second_point = input("Input the y coordinate of the second point: ")

slope_first_line = (float(y_coordinate_first_point) - 0) / (float(x_coordinate_first_point) - 0)

slope_second_line = (float(y_coordinate_second_point) - float(y_coordinate_first_point)) \
                    / (float(x_coordinate_second_point) - float(x_coordinate_first_point))

angle_in_radians = math.atan(abs(slope_first_line - slope_second_line)
                             / (1 + slope_first_line * slope_second_line))

angle_in_degrees = angle_in_radians * 180 / math.pi

turtle.speed(5)

turtle.goto(float(x_coordinate_first_point), float(y_coordinate_first_point))

turtle.write(angle_in_degrees)

turtle.goto(float(x_coordinate_second_point), float(y_coordinate_second_point))

turtle.exitonclick()

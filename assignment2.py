import math

import turtle

x_coordinate_first_point = input("Input the x coordinate of the first point: ")

y_coordinate_first_point = input("Input the y coordinate of the first point: ")

x_coordinate_second_point = input("Input the x coordinate of the second point: ")

y_coordinate_second_point = input("Input the y coordinate of the second point: ")

slope_first_line = (int(y_coordinate_first_point) - 0) / (int(x_coordinate_first_point) - 0)

slope_second_line = (int(y_coordinate_second_point) - int(y_coordinate_first_point)) \
                    / (int(x_coordinate_second_point) - int(x_coordinate_first_point))

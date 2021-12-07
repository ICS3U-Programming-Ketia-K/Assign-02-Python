#!/usr/bin/env python3
# Created by: Ketia Gaelle Kaze
# Created on: Dec. 06, 2021
# This program asks the user for the radius and height
# of a cone in cm. It then calculates and displays
# the surface area and volume.
import math


def main():
    # input
    radius = float(input("\033[1;34;38m Enter the radius of the cone (cm): "))
    height = float(input("\033[1;34;38m Enter the height of the cone (cm):"))

    # process
    area = math.pi*radius*(radius+math.sqrt(radius**2+height**2))
    volume = math.pi*radius**2*height/3

    # output
    print("")
    print("\033[1;34;38m Area = {:,.2f} cm^2". format(area))
    print("\033[1;34;38m volume = {:,.2f} cm^3".format(volume))


if __name__ == "__main__":
    main()

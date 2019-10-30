#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: October 2019
# This program solves the quadratic equation ax**2 + bx + c = 0
# with user input

# import complex math module
import math


def main():
    # This function solves the quadratic equation

    # input
    print("Enter whole numbers to solve the quadratic equation!")
    a = input("Enter a value for a : ")
    b = input("Enter a value for b : ")
    c = input("Enter a value for c : ")

    # process & output
    try:
        a_int = int(a)
        b_int = int(b)
        c_int = int(c)

        discrim = (b_int**2) - (4*a_int*c_int)

        if discrim < 0:
            print("")
            print("There are no solutions!")
        else:
            if discrim == 0:
                sol2 = (-b_int + math.sqrt(discrim))/(2*a_int)
                print("")
                print("The solution is {0}".format(sol2))
            else:
                if discrim > 0:
                    sol1 = (-b_int - math.sqrt(discrim))/(2*a_int)
                    sol2 = (-b_int + math.sqrt(discrim))/(2*a_int)
                    print("")
                    print("The solutions are {0} and {1}".format(sol1, sol2))
                else:
                    print("Something went wrong. Let's try again!")
    except Exception:
        print("")
        print("You did not sub in whole numbers!")
    finally:
        print("Lets try again!!!")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on May 2022
# This is a program that finds the smallest of 10 numbers

import random


def number_list(array):

    small_number = array[1]
    for counter in array:
        if small_number > counter:
            small_number = counter

    return small_number


def main():
    # This is the main function

    random_numbers = []
    smallest_number = 0

    # Input
    for loop_counter in range(0, 10):
        random_number = random.randint(0, 100)
        random_numbers.append(random_number)
        print("The Random Number is: {0}".format(random_number))
    print("")

    smallest_number = number_list(random_numbers)

    print("The lowest number is: {0} ".format(smallest_number))
    print("\nDone.")


if __name__ == "__main__":
    main()

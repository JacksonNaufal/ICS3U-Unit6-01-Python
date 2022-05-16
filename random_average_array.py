#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: March 2022
# This is a random number average calculator

import random


def main():

    random_number = []
    total = 0
    counter = 0
    rounded = 0
    # input
    for counter in range(10):
        random_num = random.randint(0, 100)
        random_number.append(random_num)
        print("The random number is {0}".format(random_num))

    for counter in range(10):
        total = total + random_num

    overall = sum(random_number) / len(random_number)
    rounded = round(overall, 1)
    print("\nThe average number is {0}".format(overall))

    # process


if __name__ == "__main__":
    main()

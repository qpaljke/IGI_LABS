"""
Count the number of digits in a given string
Author: Paul Shukaila
Date: 20.03.2024
"""


def get_string_input():
    while True:
        try:
            st = input('Enter a string: ')
            return st
        except Exception as e:
            print(f'Error {str(e)}')


def count_digits(x: str):
    count = 0
    for i in range(len(x)):
        if x[i].isdigit():
            count += 1

    return count


def task3():
    while True:
        try:
            inp = get_string_input()
            print('Number of digits in input string: ', count_digits(inp))
        except Exception as e:
            print(f'Error: {str(e)}')

        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != "y":
            break

"""
Count the numbers that are greater than '12'
Author: Paul Shukaila
Date: 20.03.2024
"""


def get_integer_input():
    while True:
        try:
            num = int(input('Enter an integer value: '))
            return num
        except ValueError:
            print('Wrong input')


def count_numbers():
    count = 0
    while True:
        try:
            num = get_integer_input()
        except Exception:
            raise Exception('Enter valid data')

        if num > 12:
            count += 1
        if num == 133:
            break

    return count


def task2():
    while True:
        try:
            result = count_numbers()
            print('Count of integer numbers, more than 12: ', result)
        except Exception as e:
            print(f'Error: {str(e)}')

        choice = input('Do you want to continue? (y/n): ')
        if choice.lower() != 'y':
            break

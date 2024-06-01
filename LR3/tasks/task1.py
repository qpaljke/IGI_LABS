"""
Calculate function value at a point with a given accuracy and compare it to inbuilt function
Author: Paul Shukaila
Date: 20.03.2024
"""

import pandas as pd
import math
df = pd.DataFrame()


def get_user_input():
    while True:
        try:
            x = float(input("Enter x value: "))
            eps = float(input("Enter eps value: "))
            return x, eps
        except ValueError:
            print("Wrong input")


def calculate_tailor(x, eps):
    result = 0.0
    i = 1

    while True:
        term = (-1) * (x ** i / i)
        if abs(term) < eps:
            break
        result += term
        i += 1

    df['x'] = [x]
    df['n'] = [i]
    df['F(x)'] = [result]
    df['Math F(x)'] = [math.log(1-x, math.e)]
    df['eps'] = [eps]

    return df.to_string(index=False)


def run_program():
    x, eps = get_user_input()
    result = calculate_tailor(x, eps)
    print(result)


def task1():
    while True:
        run_program()
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != "y":
            break

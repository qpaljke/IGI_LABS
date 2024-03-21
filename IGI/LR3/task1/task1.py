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
            n = int(input("Enter n value: "))
            return x, eps, n
        except ValueError:
            print("Wrong input")


def calculate_tailor(x, eps, n):
    result = 0.0
    i = 1

    while i <= n:
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
    x, eps, n = get_user_input()
    result = calculate_tailor(x, eps, n)
    print(result)


if __name__ == "__main__":
    while True:
        run_program()
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != "y":
            break

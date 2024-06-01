import tasks.task1 as t1
import tasks.task2 as t2
import tasks.task3 as t3
import tasks.task4 as t4
import tasks.task5 as t5
import os
import subprocess

def get_task_num_input():
    while True:
        try:
            num = int(input("Enter task number: "))
            if num <= 0:
                raise ValueError("Wrong input")
            return num
        except ValueError as verr:
            print(f'Value input error: {str(verr)}')


def main():
    while True:
        task_num = get_task_num_input()

        match task_num:
            case 1:
                t1.task1()
            case 2:
                t2.task2()
            case 3:
                t3.task3()
            case 4:
                t4.task4()
            case 5:
                t5.task5()
        choice = input("Exit? (y/n): ")
        if choice.lower() != "y":
            break


if __name__ == '__main__':
    main()

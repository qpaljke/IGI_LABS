from task4 import task4
from task1 import task1
from task2 import task2
from task3 import task3
from task5 import task5
from task6 import task6

if __name__ == '__main__':
    while True:
        task_inp = int(input('Choose task:\n'
                             '1: task1\n'
                             '2: task2\n'
                             '3: task3\n'
                             '4: task4\n'
                             '5: task5\n'
                             '6: task6\n'
                             '7: exit\n'))

        match task_inp:
            case 1:
                task1.run_task()
            case 2:
                task2.run_task()
            case 3:
                task3.run_task()
            case 4:
                task4.run_task()
            case 5:
                task5.run_task()
            case 6:
                task6.run_task()
            case 7:
                break

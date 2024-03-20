def get_list_len_input():
    while True:
        try:
            num = int(input("Enter list length: "))
            if num <= 0:
                raise ValueError("List length should be a positive integer")
            return num
        except ValueError as verr:
            print(f'Error: {str(verr)}')


def get_float_input():
    while True:
        try:
            num = float(input('Enter a float value: '))
            return num
        except ValueError:
            print('Wrong input')


def task5(length: int):
    lst = []
    for i in range(n):
        num = get_float_input()
        lst.append(num)

    ans_sum = 0
    first_positive_index = None
    second_positive_index = None

    for i, num in lst:
        if num > 0 and first_positive_index is None:
            first_positive_index = i
        elif num > 0 and first_positive_index is not None:
            second_positive_index = i
            break

    if second_positive_index is None:
        raise ValueError("Insufficient positive elements in the list")

    for num in lst[first_positive_index + 1:second_positive_index]:
        ans_sum += num

    print("List of elements:", lst)
    return ans_sum, max(lst, key=abs)


if __name__ == "__main__":
    while True:
        try:
            n = get_list_len_input()
            print(task5(n))
        except Exception as e:
            print(f'Error: {str(e)}')

        choice = input('Do you want to continue? (y/n): ')
        if choice.lower() != 'y':
            break

"""
1) Count the number of words that are shorter than seven characters
2) Print the shortest word ending with 'a'
3) Print the string sorted by word length
Author: Paul Shukaila
Date: 20.03.2024
"""


def task_4(x: str):
    words = x.replace(', ', ' ').split()
    count = 0
    shortest = ''
    sorted_words = sorted(x.split(), key=len)
    sorted_string = ' '.join(sorted_words)

    for word in words:
        if word.endswith('a'):
            shortest = word
            break

    for word in words:
        if len(word) < 7:
            count += 1
        if len(word) < len(shortest) and word.endswith('a'):
            shortest = word

    return count, shortest, sorted_string


def task4():
    while True:
        try:
            inp = ('So she was considering in her own mind, as well as she could, for the hot day made her feel very '
                   'sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of '
                   'getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.')
            print(task_4(inp))
        except Exception as e:
            print(f'Error: {str(e)}')

        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != "y":
            break

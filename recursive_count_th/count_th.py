'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    th_len = len('th')
    word_len = len(word)

    if word_len == 0 or word_len < th_len:
        return 0

    if word[0:th_len] == 'th':
        return count_th(word[th_len - 1:]) + 1

    return count_th(word[th_len - 1:])

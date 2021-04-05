import math

def split_list(items: list) -> list:
    # your code here
    if len(items) == 0:
        return [[], []]
    return [items[:math.ceil(len(items)/2)], items[math.ceil(len(items)/2):]]


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")

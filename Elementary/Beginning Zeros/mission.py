def beginning_zeros(number: str) -> int:
    # your code here
    a = [digit for digit in number]
    index = 0
    count = 0
    while a[index] == '0':
        count += 1
        index += 1
        if index == len(a):
            break
    return count


if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("Coding complete? Click 'Check' to earn cool rewards!")

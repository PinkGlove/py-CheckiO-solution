def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    if text.count(symbol) < 2:
        return None
    else:
        first_index = text.find(symbol, 0)
        return text.find(symbol, first_index+1)


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')

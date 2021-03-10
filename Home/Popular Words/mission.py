def popular_words(text: str, words: list) -> dict:
    # your code here
    text_split = text.split()
    words_list = []
    result = {}
    for word_split in text_split:
        words_list.append(word_split.lower())
    for word in words:
        word_count = words_list.count(word)
        result[word] = word_count
    return result


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")

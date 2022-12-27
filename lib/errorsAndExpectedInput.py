specialChars = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', ']', '[', '|', '\'', '`', ',', '.', '/', '?', ';', ':', '\'', '"', '<', '>']

malformedInput = ['%a']

urlEncodings = [f'%{hex(s)[2:].zfill(2)}' for s in range(256)]

unicodeEscapes = [f'\\u00{hex(s)[2:].zfill(2)}' for s in range(256)]

unicodeEscapes2 = [f'%u00{hex(s)[2:].zfill(2)}' for s in range(256)]

positiveNumbers = ['1' * n for n in range(1, 21)]

negativeNumbers = ['-' + '1' * n for n in range(1, 21)]

zeros = ['0' * n for n in range(1, 21)] # saw an occurance in which 000000 bypassed OTP

specialNumbers = ['2.07564741538e+16', '3.38800266804e+16', '-1.97684995314e+16', '0x481b49d0f8d5a3e7f821066157c37c', '9223372036854775808', '-9223372036854775809', '1.79769313486e+308', '2.22507385851e-308', 'inf', 'Infinity', '-Infinity']

jsonValues = ['null','[]','{}','true','false']

nulls = ['NULL', 'None', 'none', 'NaN'] # not adding null since it is in jsonValues

uuid = ['23c36ef2-84ee-11ed-a1eb-0242ac120002', '316f78f2-84ee-11ed-a1eb-0242ac120002', '91144219-b81b-4192-bd85-62ccacc976d2', 'fcd69fbd-2d45-408a-9154-4bfe611129bf']

email = ['sbfruigfasdfgreifjdg123@gmail.com'] # add a {domain} which tests for target's emails


def generate():
    wordlist = []

    wordlist = wordlist \
    + specialChars \
    + malformedInput \
    + urlEncodings \
    + unicodeEscapes \
    + unicodeEscapes2 \
    + positiveNumbers \
    + negativeNumbers \
    + zeros \
    + specialNumbers \
    + jsonValues \
    + nulls \
    + uuid \
    + email
    
    return wordlist

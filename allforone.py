#!/usr/bin/env python3
import os
import sqlalchemy
import datetime
import pytz
import string
import random
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from argparse import ArgumentParser
from lib import errorsAndExpectedInput
from lib import xss
from lib import commandInjection
from lib import sqlInjection
from lib import noSqlInjection
from lib import ssrf
from lib import crlf
from lib import ssti
from lib import xxe
from lib import log4j
from lib import pathTraversalLinux
from lib import pathTraversalWindows
from lib import sqlInjectionOracle
from lib import sqlInjectionMssql
from lib import sqlInjectionPostgresql
from lib import sqlInjectionMysql


currentDir = os.path.dirname(os.path.abspath(__file__))
databasePath = os.path.join(currentDir, "allforone.sqlite3")
engine = create_engine(f"sqlite:///{databasePath}", echo=False)
Base = declarative_base()


parser = ArgumentParser(description='')
parser.add_argument('--errors', action='store_true', help='')
parser.add_argument('--xss', action='store_true', help='')
parser.add_argument('--osi', action='store_true', help='')
parser.add_argument('--sql', action='store_true', help='')
parser.add_argument('--nosql', action='store_true', help='')
parser.add_argument('--ssrf', action='store_true', help='')
parser.add_argument('--crlf', action='store_true', help='')
parser.add_argument('--ssti', action='store_true', help='')
parser.add_argument('--xxe', action='store_true', help='')
parser.add_argument('--path-traversal-linux', action='store_true', help='')
parser.add_argument('--path-traversal-windows', action='store_true', help='')
parser.add_argument('--log4j', action='store_true', help='')
parser.add_argument('--dbms', nargs='*', help='all, oracle, mssql, postgresql, mysql') # will add a ton more
parser.add_argument('--collaborator', help='specify domain or IP', default='{collaborator}')
parser.add_argument('--time', help='specify time delay caused by payloads in seconds', default='{time}')
parser.add_argument('--ssrf-domain', help='specify a domain to use in ssrf bypasses', default='{domain}')
parser.add_argument('--note', help='note detailing what was tested and how')
parser.add_argument('--query', help='query collaborator STRING (example: STRING.{collaborator})')
args = vars(parser.parse_args())


class Payload(Base):
    __tablename__ = 'payloads'
    id = Column(Integer, primary_key=True)
    creationDate = Column(String, default=datetime.datetime.now(pytz.timezone('Asia/Jerusalem')))
    identifier = Column(String)
    payload = Column(Integer)
    note = Column(String)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def main():
    if args['query'] == None:
        wordlist()
    
    if args['query'] != None:
        query()


def wordlist():
    []
    wordlist = []
    if args['errors']:
        wordlist += errorsAndExpectedInput.generate()

    if args['xss']:
        wordlist += xss.generate()

    if args['osi']:
        wordlist += commandInjection.generate()

    if args['sql']:
        wordlist += sqlInjection.generate()

    if args['nosql']:
        wordlist += noSqlInjection.generate()

    if args['ssrf']:
        wordlist += ssrf.generate()

    if args['crlf']:
        wordlist += crlf.generate()

    if args['ssti']:
        wordlist += ssti.generate()

    if args['xxe']:
        wordlist += xxe.generate()

    if args['path_traversal_linux']:
        wordlist += pathTraversalLinux.generate()

    if args['path_traversal_windows']:
        wordlist += pathTraversalWindows.generate()

    if args['log4j']:
        wordlist += log4j.generate()

    # --path-traversal-php
    # TODO

    if args['dbms'] != None:
        if 'all' in args['dbms'] or 'oracle' in args['dbms']:
            wordlist += sqlInjectionOracle.generate()

        if 'all' in args['dbms'] or 'mssql' in args['dbms']:
            wordlist += sqlInjectionMssql.generate()

        if 'all' in args['dbms'] or 'postgresql' in args['dbms']:
            wordlist += sqlInjectionPostgresql.generate()

        if 'all' in args['dbms'] or 'mysql' in args['dbms']:
            wordlist += sqlInjectionMysql.generate()

    with open(currentDir + '\\' + 'allforoneWordlist.txt', 'w') as f:
        for word in wordlist:
            if '{collaborator}' in word:
                identifier = randomString()
                word = word.replace('{collaborator}', identifier + '.' + args['collaborator'])
                word = word.replace('{domain}', args['ssrf_domain'])
                payload = Payload(identifier=identifier, payload=word, note=args['note'])
                session.add(payload)

            if '{time}' in word:
                word = word.replace('{time}', args['time'])

            f.write(word + '\n')
        session.commit()


def query():
    identifier = args['query'].split('.')[0]
    payloads = session.query(Payload).filter(Payload.identifier == identifier).all()
    for payload in payloads:
        print()
        print('Identifier: ' + payload.identifier)
        print('Payload: ' + payload.payload)
        print('Date: ' + payload.creationDate)
        print('Note: ' + payload.note)
    print()


# TODO: change to md5
def randomString():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))


if __name__ == '__main__':
    main()


session.close()

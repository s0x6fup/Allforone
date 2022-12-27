from base64 import b64decode

# TODO: add "blind" detection codes

detectors = [
        b64decode('JHt7PCVbJScifX0lXA==').decode('ascii'),
        b64decode('JCU3QiU3QiUzQyUyNSU1QiUyNSclMjIlN0QlN0QlMjUlNUM=').decode('ascii'),
        b64decode('JCUyNTdCJTI1N0IlMjUzQyUyNTI1JTI1NUIlMjUyNSclMjUyMiUyNTdEJTI1N0QlMjUyNSUyNTVD').decode('ascii')
    ]

def generate():
    wordlist = []

    wordlist += detectors
    
    return wordlist

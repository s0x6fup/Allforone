detectors = [
        '%0d%0aLocation: https://google.com/?',
        '%3f%0d%0aLocation: https://google.com/?',
        '%0D%0ALocation: https://google.com/?',
        '%3F%0D%0ALocation: https://google.com/?'
    ]

def generate():
    wordlist = []

    wordlist += detectors
    
    return wordlist

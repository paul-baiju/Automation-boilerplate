import requests
r = requests.get('https://github.com/kennethreitz/requests/blob/master/README.rst')
'Requests:' in r.text
r.headers['Content-Type']
'text/html; charset=utf-8'
r = requests.get('https://raw.github.com/kennethreitz/requests/master/README.rst')
'Requests:' in r.text
r.headers['Content-Type']
'text/plain; charset=utf-8'
print (r.text)
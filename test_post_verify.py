import urllib.parse, urllib.request, re
url='http://127.0.0.1:5000/'
data=urllib.parse.urlencode({'text':'Hi'}).encode()
resp=urllib.request.urlopen(url, data=data)
html=resp.read().decode()
m=re.search(r'<h1>(.*?)</h1>', html, re.S)
print(m.group(1).strip() if m else 'NO H1')

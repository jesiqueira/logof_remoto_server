from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


# url_vdi = "link/"

hdr = {'User-Agent': 'Mozilla/5.0'}
# print(dir(Request))
req = Request(url_vdi, headers=hdr)
response_vdi = urlopen(req)
html_vdi = response_vdi.read()
html_vdi


# request = Request(url_vdi)

# response_vdi = urlopen(request)
# html_vdi = response_vdi.read()
# print(html_vdi)
# print(r.ok)
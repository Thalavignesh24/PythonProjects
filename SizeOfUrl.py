# import urllib.request
# #importing the module
# file = urllib.request.urlopen("")
# #just a dummy file

# print(file.length)

import requests
#importing the requests module
url = "https://www.mongodb.com/community/forums/t/case-insensitive-search-with-regex/120598/12"
#just a dummy file URL
info = requests.head(url)
#fetching the header information
print(info.headers,"\n\n")
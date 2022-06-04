# import  urllib.request
# opener = urllib.request.build_opener()
# response = opener.open("https://httpbin.org/get")
# print(response.read())

import  requests
response = requests.post("https://httpbin.org/post", data="test Data", headers={"h1":"test Title"})


print(response.text)

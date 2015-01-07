import urllib.parse
import http.client

szURL = "http://c1.img.netmarble.kr/web/netmarble/main/v/img/logo.gif"


httpConnection = http.client.HTTPConnection("c1.img.netmarble.kr")
httpConnection.request("GET", "/web/netmarble/main/v/img/logo.gif")
httpResponse = httpConnection.getresponse()

print("Content-length:",httpResponse.length)
print("Reponse code:",httpResponse.status)

fpWirte = open("./download.gif", "wb")
fpWirte.write(httpResponse.read())
fpWirte.close()

import urllib.request as req
import urllib.parse as par

url="http://127.0.0.1:3000/account"

values={
    "account":"lou8168168",
    "password":"lou10130244",
    "member":"generalMember"
}

data=par.urlencode(values,encoding="utf-8")
data=data.encode("ascii")
request=req.Request(url,data)
with req.urlopen(request) as response:
    result=response.read().decode("utf-8")
print(result)

with open("hack.html",mode="w",encoding="utf-8") as file:
    file.write(result)
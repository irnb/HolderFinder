import requests
import json
import time

res = requests.get("https://apilist.tronscan.org/api/accountv2?address=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t&source=true")
#res = json.loads(res.text)
print(res.text)
print("==========================================================================================================================")
res = requests.get("https://apilist.tronscan.org/api/accountv2?address=TWWzKG826bbhkAKNa2FE1UTdD7FT9dsmjs&source=true")
#res = json.loads(res.text)
print(res.text)

# trx_balance = None
# for item in res["withPriceTokens"]:
#     print(item["tokenId"],item["tokenName"],int(item["balance"])/ 10 ** int(item["tokenDecimal"]))
#     print(type(item["tokenName"]), item["tokenName"])
#     print(item)

# print("==========================================================================================================================")
# res = requests.get("https://apilist.tronscan.org/api/transfer?sort=-timestamp&count=true&limit=20&start=0&address=TJfR6ycEZfct88kLgLyKv4PefyrPBMuSPs")
# res = json.loads(res.text)
# print(res)

# print("==========================================================================================================================")

# res = requests.get("https://apilist.tronscan.org/api/token_trc20/transfers?limit=20&start=0&sort=-timestamp&count=true&relatedAddress=TJfR6ycEZfct88kLgLyKv4PefyrPBMuSPs")
# res = json.loads(res.text)
# print(res)

# print("==========================================================================================================================")

# x = "https://apilist.tronscan.org/api/transaction?sort=-timestamp&count=true&limit=40&start=0&address=TNAoh4TzZJLXjByVwYx4RP6uJFVv2SRD7s"
# res = requests.get(x)
# res = json.loads(res.text)
# print(res["total"])
# print(len(res["data"]), type(res["data"]))
# for index, item in enumerate( res["data"] ):
#     print("=================================================================================")
#     print(index+1, item)



# for data in res["data"]:
#     print (data)
# print("==========================================================================================================================")

# x = "https://apilist.tronscan.org/api/transaction?sort=-timestamp&count=true&limit=40&start=40&address=TNAoh4TzZJLXjByVwYx4RP6uJFVv2SRD7s"
# res = requests.get(x)
# res = json.loads(res.text)
# print(res["total"])
# print((len(res["data"])))
# print(res)
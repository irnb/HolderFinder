withdrawTxId = [
    "97c998cc988b402cbcc3757eaad4c1acdd8fe5f91d38ca4d0485333bbc88d373",
    "e81d42f52f9176c2fa0943db7186e9e56619ca427258164b2fde2dcd5dbc4975",
    "3ed60b8e3d7cd0cbaba336589de9e7b804d7e08b1f18f5942c957a469ecc284a",
]


# import requests

# url = "https://api.trongrid.io/wallet/createtransaction"

# payload = '{\n    "to_address": "41e9d79cc47518930bc322d9bf7cddd260a0260a8d",\n    "owner_address": "41D1E7A6BC354106CB410E65FF8B181C600FF14292",\n    "amount": 1000\n}'
# headers = {
#     "Content-Type": "application/json",
#     "TRON-PRO-API-KEY": "25f66928-0b70-48cd-9ac6-da6f8247c663",
# }
# response = requests.request("POST", url, data=payload, headers=headers)
# print(response.text)

# import requests

# url = "https://api.shasta.trongrid.io/v1/accounts/TPMF2n3hJLcCwoHq6bwLeVXBbNZgj73AEd/transactions"

# headers = {"Accept": "application/json"}

# response = requests.request("GET", url, headers=headers)


import requests

data = '{"value": "3ed60b8e3d7cd0cbaba336589de9e7b804d7e08b1f18f5942c957a469ecc284a"}'

response = requests.post('https://api.trongrid.io/wallet/gettransactionbyid', data=data)

print(response.text)
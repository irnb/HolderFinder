from tronapi import Tron, HttpProvider
import base58
import requests
import json
import time


full_node = HttpProvider("https://api.trongrid.io")
solidity_node = HttpProvider("https://api.trongrid.io")
event_server = "https://api.trongrid.io"

Min_usdt_balance_for_hotwallet = 1000
Min_trx_balance_for_hotwallet = 1000
min_tx_count_for_hot_wallet = 25


min_usdt_balance_for_holder = 1000
max_tx_count_for_holder = 20
min_trx_balance_for_holder = 2000

#Add date 

tron = Tron(full_node=full_node, solidity_node=solidity_node, event_server=event_server)


# get usdt reciver
# tron.trx.get_transaction_info
# >>> abi ='''[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_upgradedAddress","type":"address"}],"name":"deprecate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"deprecated","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_evilUser","type":"address"}],"name":"addBlackList","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"upgradedAddress","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"maximumFee","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_maker","type":"address"}],"name":"getBlackListStatus","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_subtractedValue","type":"uint256"}],"name":"decreaseApproval","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_value","type":"uint256"}],"name":"calcFee","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"oldBalanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"newBasisPoints","type":"uint256"},{"name":"newMaxFee","type":"uint256"}],"name":"setParams","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"issue","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_addedValue","type":"uint256"}],"name":"increaseApproval","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"redeem","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"basisPointsRate","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"isBlackListed","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_clearedUser","type":"address"}],"name":"removeBlackList","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"MAX_UINT","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_blackListedUser","type":"address"}],"name":"destroyBlackFunds","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_initialSupply","type":"uint256"},{"name":"_name","type":"string"},{"name":"_symbol","type":"string"},{"name":"_decimals","type":"uint8"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_blackListedUser","type":"address"},{"indexed":false,"name":"_balance","type":"uint256"}],"name":"DestroyedBlackFunds","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount","type":"uint256"}],"name":"Issue","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount","type":"uint256"}],"name":"Redeem","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"newAddress","type":"address"}],"name":"Deprecate","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_user","type":"address"}],"name":"AddedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_user","type":"address"}],"name":"RemovedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"feeBasisPoints","type":"uint256"},{"indexed":false,"name":"maxFee","type":"uint256"}],"name":"Params","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"previousOwner","type":"address"},{"indexed":true,"name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]'''
# response = tron.trx.get_transaction_info("cd37d0e8a78fab890e4171b1381247bd7fa355615a83fb9ecbf089b78cf1ba26")
# >>> contract= tron.trx.contract("TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",abi=abi)
# contract.tron.get_event_transaction_id("cd37d0e8a78fab890e4171b1381247bd7fa355615a83fb9ecbf089b78cf1ba26")
# >>> contract.tron.get_event_transaction_id("cd37d0e8a78fab890e4171b1381247bd7fa355615a83fb9ecbf089b78cf1ba26")[0]["result"]['1']
#'0x4fd9fbd016f4c552f3962d499b41efbacdf392b9'
# >>> import base58
# >>> base58.b58encode_check(bytes.fromhex("414fd9fbd016f4c552f3962d499b41efbacdf392b9")) "+41 first of hex"
# b'THFRWyx5cQme3Mv2nuuPVRarany86fE7by'
# str(base58.b58encode_check(bytes.fromhex("414fd9fbd016f4c552f3962d499b41efbacdf392b9")))[2:-1]


final_result = []
#####################check be uniq answer

usdt_abi = """[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_upgradedAddress","type":"address"}],"name":"deprecate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"deprecated","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_evilUser","type":"address"}],"name":"addBlackList","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"upgradedAddress","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"maximumFee","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_maker","type":"address"}],"name":"getBlackListStatus","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_subtractedValue","type":"uint256"}],"name":"decreaseApproval","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_value","type":"uint256"}],"name":"calcFee","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"oldBalanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"newBasisPoints","type":"uint256"},{"name":"newMaxFee","type":"uint256"}],"name":"setParams","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"issue","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_addedValue","type":"uint256"}],"name":"increaseApproval","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"redeem","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"basisPointsRate","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"isBlackListed","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_clearedUser","type":"address"}],"name":"removeBlackList","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"MAX_UINT","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_blackListedUser","type":"address"}],"name":"destroyBlackFunds","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_initialSupply","type":"uint256"},{"name":"_name","type":"string"},{"name":"_symbol","type":"string"},{"name":"_decimals","type":"uint8"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_blackListedUser","type":"address"},{"indexed":false,"name":"_balance","type":"uint256"}],"name":"DestroyedBlackFunds","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount","type":"uint256"}],"name":"Issue","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount","type":"uint256"}],"name":"Redeem","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"newAddress","type":"address"}],"name":"Deprecate","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_user","type":"address"}],"name":"AddedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_user","type":"address"}],"name":"RemovedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"feeBasisPoints","type":"uint256"},{"indexed":false,"name":"maxFee","type":"uint256"}],"name":"Params","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"previousOwner","type":"address"},{"indexed":true,"name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]"""
USDT_addr = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"


def trx_finder(txids: list):
    # 1: get sender of this transaction
    # 2: check the sender is hot wallet or not
    # 3: if it is a hotwallet then get all transaction this adress is send to the network
    # 4: and then call tx_analysis for each transaction

    for txid in txids:
        tx = tron.trx.get_transaction(txid)
        from_addr = tx["raw_data"]["contract"][0]["parameter"]["value"]["owner_address"]
        from_addr = str(base58.b58encode_check(bytes.fromhex(str(from_addr))))[2:-1]
        
        try:
            if is_hot_wallet(from_addr):

                res = requests.get(
                    "https://apilist.tronscan.org/api/accountv2?address="
                    + from_addr
                    + "&source=true"
                )
                res = json.loads(res.text)
                tx_count = res["totalTransactionCount"]
                limit = 40

                pages = limit_and_start(limit, tx_count)

                last_line = 0
                for page in pages:
                    url = (
                        "https://apilist.tronscan.org/api/transaction?sort=-timestamp&count=true&limit="
                        + str(limit)
                        + "&start="
                        + page
                        + "&address="
                        + from_addr
                    )
                    res = requests.get(url)
                    res = json.loads(res.text)
                    if res["total"] == 0:
                        continue
                    last_line = tx_analysis(res["data"], from_addr, last_line)
                    time.sleep(0.25)
        except:
            continue
    return final_result



def tx_analysis(results, from_addr: str, lastLine: int):
    # 1- check the transaction is sent tx not a recive
    # 2- find reciver address in token or trx send
    # 3- check token holder
    # 4- check it is a trx holder or not
    # print result in console for abserve progress of running script should be done in this function
    line = lastLine
    for result in results:
        try:
            if result["toAddress"] == from_addr:
                print(line, "#1", "this is a recive transaction")
                line = line + 1
                continue
            elif not (result["result"] == "SUCCESS"):
                continue

            to_addr = ""

            if result["toAddress"] == USDT_addr:
                # finde recive address with using of usdt contract event
                USDT = tron.trx.contract(USDT_addr, abi=usdt_abi)
                info = USDT.tron.get_event_transaction_id(result["hash"])[0]["result"]["to"]
                to_addr = str(base58.b58encode_check(bytes.fromhex("41" + info[2:])))[2:-1]
                check = is_holder(to_addr)
                if check:
                    print(line, "#2", "good", "a usdt holder is finded", to_addr)
                    line = line + 1
                    if not (to_addr in final_result):
                        final_result.append(to_addr)
                else:
                    print(line, "#2.1", "not a usdt holder")
                line = line + 1
            else:
                if not (result["contractType"] == 1) or result["amount"] == str(0):
                    print(
                        line,
                        "#3",
                        "other token contract or trx value is zero",
                        result["to"],
                        result["value"],
                    )
                    line = line + 1
                    continue

                to_addr = result["toAddress"]
                check = is_holder(to_addr)

                if check:
                    print(line, "#4", "good", "a trx holder is finded")
                    line = line + 1
                    final_result.append(to_addr)
                else:
                    print(line, "#4.1", "not a trx holder")
                line = line + 1
        except:
            continue


    return line


def is_holder(addr: str):
    # check balance and not be a hot wallet
    check = is_hot_wallet(addr)
    if check:
        return False


    res = requests.get(
        "https://apilist.tronscan.org/api/accountv2?address=" + addr + "&source=true"
    )
    res = json.loads(res.text)
    tx_count = res["totalTransactionCount"]

    trx_balance_is_found = False
    usdt_balance_is_found = False

    usdt_balance = 0
    trx_balance = 0
    for item in res["withPriceTokens"]:
        if not trx_balance_is_found:
            if item["tokenId"] == "_" and item["tokenAbbr"] == "trx":
                trx_balance = int(item["balance"]) / 10 ** int(item["tokenDecimal"])
                trx_balance_is_found = True
        elif not usdt_balance_is_found:
            if (
                item["tokenId"] == "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"
                and item["tokenAbbr"] == "USDT"
            ):
                usdt_balance = int(item["balance"]) / 10 ** int(item["tokenDecimal"])
                usdt_balance_is_found = True
        else:
            break

    if (
        (usdt_balance >= min_usdt_balance_for_holder)
        or (trx_balance >= min_trx_balance_for_holder)
    ) and (tx_count <= max_tx_count_for_holder):
        return True


def is_hot_wallet(addr: str):
    # check balance and tx count
    res = requests.get(
        "https://apilist.tronscan.org/api/accountv2?address=" + addr + "&source=true"
    )
    # print(addr)
    # print(res.status_code)
    res = json.loads(res.text)
    tx_count = res["totalTransactionCount"]

    trx_balance_is_found = False
    usdt_balance_is_found = False

    usdt_balance = 0
    trx_balance = 0
    for item in res["withPriceTokens"]:
        if not trx_balance_is_found:
            if item["tokenId"] == "_" and item["tokenAbbr"] == "trx":
                trx_balance = int(item["balance"]) / 10 ** int(item["tokenDecimal"])
                trx_balance_is_found = True
                continue
        elif not usdt_balance_is_found:
            if (
                item["tokenId"] == "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"
                and item["tokenAbbr"] == "USDT"
            ):
                usdt_balance = int(item["balance"]) / 10 ** int(item["tokenDecimal"])
                usdt_balance_is_found = True
                continue
        else:
            break

    if (tx_count >= min_tx_count_for_hot_wallet) and (
        usdt_balance >= Min_usdt_balance_for_hotwallet
        or trx_balance >= Min_trx_balance_for_hotwallet
    ):
        return True
    else:
        return False


def limit_and_start(limit: int, transaction_count: int):
    r = transaction_count // limit
    k = transaction_count % limit

    if k > 0:
        r = r + 1

    # return style : [start1,start2,....]
    # example : limit_and_start(40,45) => [0,40]
    # example : limit_and_start(40,94) => [0,40,80]
    return [str(i * 40) for i in range(r)]


if __name__ == "__main__":
    # use for testing function of this file
    # print(is_hot_wallet("TNAoh4TzZJLXjByVwYx4RP6uJFVv2SRD7s"))
    results = trx_finder(txids=["97c998cc988b402cbcc3757eaad4c1acdd8fe5f91d38ca4d0485333bbc88d373"])
    # print(is_hot_wallet("TGc3sq7zrT2BxRrxFjxdrLnxuEBNhJtP1N"))

    #write final result in a file 
    
    # textfile = open("result.txt", "w")
    # for element in results:
    #     textfile.write(element + "\n")
    # textfile.close()

    # textfile = open("info.txt", "w")
    # textfile.write("Tron\n"+"result is in ","result.txt" + "\n"+"len :", len(results))
    # textfile.close()

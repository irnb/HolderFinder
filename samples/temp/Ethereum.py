from eth_typing import abi
import hexbytes
from web3 import Web3
import json
import requests
import time

web3 = Web3(
    Web3.HTTPProvider("https://mainnet.infura.io/v3/64108f9ca2894871b8ee3478a3135021")
)

api_key = "JKKNXYTW3WFTV925T3FRQMU4A4VYK9Y27E"

USDT_addr = "0xdAC17F958D2ee523a2206206994597C13D831ec7"

usdt_abi = """[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_upgradedAddress","type":"address"}],"name":"deprecate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"deprecated","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_evilUser","type":"address"}],"name":"addBlackList","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"upgradedAddress","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balances","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"maximumFee","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_maker","type":"address"}],"name":"getBlackListStatus","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowed","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getOwner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"newBasisPoints","type":"uint256"},{"name":"newMaxFee","type":"uint256"}],"name":"setParams","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"issue","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"redeem","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"basisPointsRate","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"isBlackListed","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_clearedUser","type":"address"}],"name":"removeBlackList","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"MAX_UINT","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_blackListedUser","type":"address"}],"name":"destroyBlackFunds","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_initialSupply","type":"uint256"},{"name":"_name","type":"string"},{"name":"_symbol","type":"string"},{"name":"_decimals","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount","type":"uint256"}],"name":"Issue","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount","type":"uint256"}],"name":"Redeem","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"newAddress","type":"address"}],"name":"Deprecate","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"feeBasisPoints","type":"uint256"},{"indexed":false,"name":"maxFee","type":"uint256"}],"name":"Params","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_blackListedUser","type":"address"},{"indexed":false,"name":"_balance","type":"uint256"}],"name":"DestroyedBlackFunds","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_user","type":"address"}],"name":"AddedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_user","type":"address"}],"name":"RemovedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"}]"""


min_tx_count_for_hot_wallet = 10

max_tx_count_for_holder = 25

min_usdt_balance_for_hot_wallet = 10000

min_eth_balance_for_hot_wallet = 100

min_usdt_balance_for_holder = 1000

min_eth_balance_for_holder = 1

final_result = []


def eth_finder(txid: str):
    tx = web3.eth.getTransaction(txid)
    tx = web3.toJSON(tx)
    tx = json.loads(tx)

    from_addr = tx["from"]

    if is_hot_wallet(from_addr):
        tx_count = web3.eth.getTransactionCount(from_addr)
        # print(tx_count)
        offset = 1000
        pages, last_offset = page_and_offset(tx_count, offset)
        # print(pages,last_offset)

        last_page = pages[-1]
        last_line = 0
        for page in pages:
            if page == last_page:
                offset = last_offset

            url = (
                "https://api.etherscan.io/api?module=account&action=txlist&address="
                + from_addr
                + "&startblock=0&endblock=99999999&page="
                + page
                + "&offset="
                + str(offset)
                + "&sort=asc&apikey="
                + api_key
            )
            # print(url)
            response = requests.get(url)
            response = json.loads(response.text)
            # print(response)
            if response["status"] == "0":
                continue
            last_line = tx_analysis(response["result"], from_addr, last_line)
            time.sleep(0.25)

    return final_result


def page_and_offset(transaction_count: int, offset: int):
    r = transaction_count // offset
    k = transaction_count % offset

    if k > 0:
        r = r + 1

    return [str(i + 1) for i in range(r)], k


def tx_analysis(results, from_addr: str, lastLine: int):
    # print(results)
    # print(type(results))
    line = lastLine

    for result in results:
        if result["to"] == from_addr:
            print(line, "#1", "this is a recive transaction")
            line = line + 1
            continue

        to_addr = ""
        if result["to"] == USDT_addr:
            USDT = web3.eth.contract(address=USDT_addr, abi=usdt_abi)
            receipt = web3.eth.getTransactionReceipt(result["hash"])
            logs = USDT.events.Transfer().processReceipt(receipt)

            to_addr == logs[0].args.to


            check = is_holder(to_addr)
            if check:
                print(line, "#2", "good", "a usdt holder is finded", to_addr)
                line = line + 1
                final_result.append(to_addr)
            print(line, "#2.1", "not a usdt holder")
            line = line + 1
        else:
            if is_contract(result["to"]) or result["value"] == str(0):
                print(
                    line,
                    "#3",
                    "other token contract or eth value is zero",
                    result["to"],
                    result["value"],
                )
                line = line + 1
                continue

            to_addr = result["to"]
            check = is_holder(to_addr)

            if check:
                print(line, "#4", "good", "a eth holder is finded")
                line = line + 1
                final_result.append(to_addr)
            print(line, "#4.1", "not a eth holder")
            line = line + 1

    return line


def is_holder(addr: str):
    addr = web3.toChecksumAddress(addr)
    # check it's not hot wallet
    # get balance and check with min balance eth and usdt
    # get tx count and its not exchange account (tx count + checking latest tx destiny) -> خب عتیقه وقتی درست باشه در اصل موجودی هم نباید داشته باشه چون اکسچنج خالی میکمنه دیگه پس حواست باشه
    check = is_hot_wallet(addr)
    if check:
        return False

    tx_count = web3.eth.getTransactionCount(addr)

    USDT = web3.eth.contract(USDT_addr, abi=usdt_abi)
    decimals = USDT.functions.decimals().call()
    DECIMALS = 10 ** decimals
    usdt_balance = USDT.functions.balanceOf(addr).call()
    usdt_balance = usdt_balance // DECIMALS

    eth_balance = web3.eth.get_balance(addr)
    eth_balance = web3.fromWei(eth_balance, "ether")

    if (
        (usdt_balance >= min_usdt_balance_for_holder)
        or (eth_balance >= min_eth_balance_for_holder)
    ) and (tx_count <= max_tx_count_for_holder):
        return True


def is_hot_wallet(addr: str):
    addr = web3.toChecksumAddress(addr)

    tx_count = web3.eth.getTransactionCount(addr)

    USDT = web3.eth.contract(USDT_addr, abi=usdt_abi)
    decimals = USDT.functions.decimals().call()
    DECIMALS = 10 ** decimals
    usdt_balance = USDT.functions.balanceOf(addr).call()
    usdt_balance = usdt_balance // DECIMALS

    eth_balance = web3.eth.get_balance(addr)
    eth_balance = web3.fromWei(eth_balance, "ether")

    if (tx_count >= min_tx_count_for_hot_wallet) and (
        usdt_balance >= min_usdt_balance_for_hot_wallet
        or eth_balance >= min_eth_balance_for_hot_wallet
    ):
        return True
    else:
        return False


def is_contract(addr: str):
    addr = web3.toChecksumAddress(addr)
    temp = web3.eth.getCode(addr)
    if temp != hexbytes.main.HexBytes(""):
        return True
    else:
        return False


if __name__ == "__main__":
    print(
        eth_finder("0xe3636d43d2c7b99677f22c9257af051b22a3db917d36e1f303d9a469c7233658")
    )

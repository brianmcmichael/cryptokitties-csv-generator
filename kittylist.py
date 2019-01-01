import json
import csv
import os
import time
from web3.auto import w3

start_time = time.time()

#print(w3.eth.getBlock('latest'))

CONTRACT_ABI = ""
with open(os.path.join(os.path.dirname(__file__), "cryptokitties.json")) as json_data:
	abi_json = json.load(json_data)
	# print(abi_json)
	CONTRACT_ABI = abi_json['result']

#print(CONTRACT_ABI)

kittyContract = w3.eth.contract(
	address="0x06012c8cf97BEaD5deAe237070F9587f8E7A266d",
	abi=CONTRACT_ABI
)


print(kittyContract.functions.name().call())

_supply = int(kittyContract.functions.totalSupply().call())

print(f"Getting {_supply} kitties")

# isGestating bool, 
# isReady bool, 
# cooldownIndex uint256, 
# nextActionAt uint256, 
# siringWithId uint256, 
# birthTime uint256, 
# matronId uint256, 
# sireId uint256, 
# generation uint256, 
# genes uint256

start_id = 0
read_file = False

if os.path.exists('kittylist.csv'):
    file_flag = 'a'
    read_file = True
else:
    file_flag = 'w'

if read_file:
    with open('kittylist.csv', 'r') as kittylist:
        last_line = list(kittylist)[-1]
        last_id = int(last_line.split(',')[0])
        start_id = last_id + 1

print(f"Starting with {start_id}")

with open('kittylist.csv', file_flag) as outcsv:
    _headers = [ "id", "isGestating", "isReady", "cooldownIndex", "nextActionAt",
                 "siringWithId", "birthTime", "matronId", "sireId",
                 "generation", "genes" ]
    writer = csv.DictWriter(outcsv, fieldnames = _headers)
    if not read_file:
        writer.writeheader()

    _kitties = []

    for _id in range(start_id, _supply):
        _k = kittyContract.functions.getKitty(_id).call()
        writer.writerow({
            "id": _id,
            "isGestating": _k[0],
            "isReady": _k[1],
            "cooldownIndex": _k[2],
            "nextActionAt": _k[3],
            "siringWithId": _k[4],
            "birthTime": _k[5],
            "matronId": _k[6],
            "sireId": _k[7],
            "generation": _k[8],
            "genes": _k[9]
        })


elapsed_time = time.time() - start_time

print(f"Got {_supply + 1} kitties in {elapsed_time} seconds")

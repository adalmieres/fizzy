import json
import requests

with open('api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']


START_BLOCK = 5746477
addNewInsurance = "0x740610c472095940dbb97134b5a7c4f27fb03c69bd892fea239850fa66dc5480"
updateFlightStatus = "0x1a6e2df3135fe8e5b7327d8181b265f9d5b7c981402cd1b82faf820f0cc054bd"
CONTRACT = "0xe083515d1541f2a9fd0ca03f189f5d321c73b872"

'''
https://api.etherscan.io/api
?module=logs
&action=getLogs
&fromBlock=5746477
&toBlock=latest
&address=0xe083515d1541f2a9fd0ca03f189f5d321c73b872
&topic0=0x740610c472095940dbb97134b5a7c4f27fb03c69bd892fea239850fa66dc5480
&apikey=

https://api.etherscan.io/api
?module=transaction
&action=getstatus
&txhash=0x15f8e5ea1079d9a0bb04a4c58ae5fe7654b5b2b4463375ff7ffb490aa0032f3a
&apikey=YourApiKeyToken
'''

# Init
fromBlock = START_BLOCK
toBlock = "latest"

# Get first request and dump it to file
url = f"https://api.etherscan.io/api?module=logs&action=getLogs&fromBlock={START_BLOCK!s}&toBlock={toBlock!s}&address={CONTRACT!s}&topic0={addNewInsurance!s}&apikey={key!s}"
print(url)
r = requests.get(url)
data = json.loads(r.text)['result']
fullData = data

# init loop for first topic
previousData = ""
nbElements = len(data)
fromBlock = int(data[nbElements - 1]['blockNumber'],16)

while True :
    previousData = data

    url = f"https://api.etherscan.io/api?module=logs&action=getLogs&fromBlock={fromBlock!s}&toBlock={toBlock!s}&address={CONTRACT!s}&topic0={addNewInsurance!s}&apikey={key!s}"
    print(url)
    r = requests.get(url)
    data = json.loads(r.text)['result']
    
    nbElements = len(data)
    fromBlock = int(data[nbElements - 1]['blockNumber'],16)

    if previousData == data :
        break

    fullData = fullData + data
    print(f"{len(fullData)} : items")

# store data from first topic
fullData1 = fullData

# start again for second topic
# Get first request and dump it to file
url = f"https://api.etherscan.io/api?module=logs&action=getLogs&fromBlock={START_BLOCK!s}&toBlock={toBlock!s}&address={CONTRACT!s}&topic0={updateFlightStatus!s}&apikey={key!s}"
print(url)
r = requests.get(url)
data = json.loads(r.text)['result']
fullData = data

# init loop for first topic
previousData = ""
nbElements = len(data)
fromBlock = int(data[nbElements - 1]['blockNumber'],16)

while True :
    previousData = data

    url = f"https://api.etherscan.io/api?module=logs&action=getLogs&fromBlock={fromBlock!s}&toBlock={toBlock!s}&address={CONTRACT!s}&topic0={updateFlightStatus!s}&apikey={key!s}"
    print(url)
    r = requests.get(url)
    data = json.loads(r.text)['result']
    
    nbElements = len(data)
    fromBlock = int(data[nbElements - 1]['blockNumber'],16)

    if previousData == data :
        break

    fullData = fullData + data
    print(f"{len(fullData)} : items")

fullData = fullData + fullData1

#write to file
with open('data/eventLog.json', 'w') as json_file:
        json.dump(fullData, json_file, indent=4)

print("END")



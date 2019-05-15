import json
import requests

with open('api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']


START_BLOCK = 5746477
CONTRACT = "0xe083515d1541f2a9fd0ca03f189f5d321c73b872"

'''
http://api.etherscan.io/api
?module=account
&action=txlist
&address=0xe083515d1541f2a9fd0ca03f189f5d321c73b872
&startblock=0
&endblock=99999999
&sort=asc
&apikey=YourApiKeyToken
'''

# Init
url = f"https://api.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey={key!s}"
r = requests.get(url)
fromBlock = START_BLOCK
toBlock = int(json.loads(r.text)['result'],16)

# Get first request and dump it to file
url = f"http://api.etherscan.io/api?module=account&action=txlist&address={CONTRACT!s}&startblock={START_BLOCK!s}&endblock={toBlock!s}&sort=asc&apikey={key!s}"
print(url)
r = requests.get(url)
data = json.loads(r.text)['result']
fullData = data

# init loop for first topic
previousData = ""
nbElements = len(data)
fromBlock = int(data[nbElements - 1]['blockNumber'])

while True :
    previousData = data

    url = f"http://api.etherscan.io/api?module=account&action=txlist&address={CONTRACT!s}&startblock={fromBlock!s}&endblock={toBlock!s}&sort=asc&apikey={key!s}"
    print(url)
    r = requests.get(url)
    data = json.loads(r.text)['result']
    
    nbElements = len(data)
    fromBlock = int(data[nbElements - 1]['blockNumber'])

    if previousData == data :
        break

    fullData = fullData + data
    print(f"{len(fullData)} : items")


#write to file
with open('data/transactions.json', 'w') as json_file:
        json.dump(fullData, json_file, indent=4)

print("END")



# It runs perfectly so have fun with it, by Gaurav Yadav
from web3 import Web3
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Connect to an Ethereum node YOU CAN REPLACE YOUR OWN INFURA API KEY HERE
infura_url = "https://mainnet.infura.io/v3/1bcfde3dc4ca43f7b39d998c63efbdff"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if connection is successful
if web3.isConnected():
    logger.info("Connected to Ethereum node")
else:
    logger.error("Failed to connect to Ethereum node")
    exit(1)

# ABI for the Deposit Contract
contract_abi = '''
[
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "bytes",
				"name": "pubkey",
				"type": "bytes"
			},
			{
				"indexed": false,
				"internalType": "bytes",
				"name": "withdrawal_credentials",
				"type": "bytes"
			},
			{
				"indexed": false,
				"internalType": "bytes",
				"name": "amount",
				"type": "bytes"
			},
			{
				"indexed": false,
				"internalType": "bytes",
				"name": "signature",
				"type": "bytes"
			},
			{
				"indexed": false,
				"internalType": "bytes",
				"name": "index",
				"type": "bytes"
			}
		],
		"name": "DepositEvent",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "bytes",
				"name": "pubkey",
				"type": "bytes"
			},
			{
				"internalType": "bytes",
				"name": "withdrawal_credentials",
				"type": "bytes"
			},
			{
				"internalType": "bytes",
				"name": "signature",
				"type": "bytes"
			},
			{
				"internalType": "bytes32",
				"name": "deposit_data_root",
				"type": "bytes32"
			}
		],
		"name": "deposit",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "get_deposit_count",
		"outputs": [
			{
				"internalType": "bytes",
				"name": "",
				"type": "bytes"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "get_deposit_root",
		"outputs": [
			{
				"internalType": "bytes32",
				"name": "",
				"type": "bytes32"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bytes4",
				"name": "interfaceId",
				"type": "bytes4"
			}
		],
		"name": "supportsInterface",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "pure",
		"type": "function"
	}
]
'''

# Address of the Beacon Deposit Contract
contract_address = "0x00000000219ab540356cBB839Cbe05303d7705Fa"

deposit_contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# DepositEvent Process
def handle_deposit_event(event):
    logger.info("Deposit Event Detected")
    logger.info(f"Pubkey: {event['args']['pubkey'].hex()}")
    logger.info(f"Withdrawal Credentials: {event['args']['withdrawal_credentials'].hex()}")
    logger.info(f"Amount: {int.from_bytes(event['args']['amount'], byteorder='little')} Gwei")
    logger.info(f"Signature: {event['args']['signature'].hex()}")
    logger.info(f"Index: {int.from_bytes(event['args']['index'], byteorder='little')}")

# Function to monitor the deposit contract for events
def monitor_deposits():
    logger.info("Starting deposit monitoring...")
    deposit_event_filter = deposit_contract.events.DepositEvent.createFilter(fromBlock="latest")

    while True:
        for event in deposit_event_filter.get_new_entries():
            handle_deposit_event(event)
        
        web3.middleware_onion.sleep(10)

if __name__ == "__main__":
    monitor_deposits()

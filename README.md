# EtheriumDepositTracker
This project consists of a Solidity smart contract for Ethereum 2.0 deposits and a Python script that uses Web3.py to monitor deposit events via an RPC connection to an Ethereum node, such as Infura. It tracks and logs deposit details in real-time.

# Ethereum Deposit Tracker

This repository contains two main components for tracking Ethereum deposits:

1. **DepositContract.sol** - The Ethereum smart contract for handling deposit events.
2. **deposit_tracker.py** - The Python script for monitoring deposit events from the Ethereum network.

## Contents

- [DepositContract.sol](#depositcontractsol)
- [deposit_tracker.py](#deposit_trackerpy)
- [Setup and Deployment](#setup-and-deployment)
- [Usage](#usage)
- [Additional Notes](#additional-notes)

## DepositContract.sol
### Overview
`DepositContract.sol` is a Solidity smart contract designed to handle Ethereum 2.0 deposit events. It provides the following functionalities:
- **DepositEvent**: Logs deposit events with details such as public key, withdrawal credentials, amount, signature, and index.
- **deposit**: Allows users to make deposits and emits `DepositEvent`.
- **get_deposit_count**: Returns the current count of deposits.
- **get_deposit_root**: Returns the current deposit root hash.
- **supportsInterface**: Checks if the contract supports a specific interface.

###deposit_tracker.py is a Python script that monitors deposit events from the Ethereum Beacon Deposit Contract using the Web3.py library. It performs the following tasks:

- **Connects to an Ethereum Node: Uses Infura or another Ethereum node provider.
- **Interacts with the Deposit Contract: Listens for DepositEvent logs from the contract.
- **Processes Deposit Events: Logs event details such as public key, withdrawal credentials, amount, signature, and index.
###Requirements
##Before running the script, make sure you have the following installed:
- **Python 3.x
- **web3 library

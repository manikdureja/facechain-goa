import os
import hashlib
from web3 import Web3

def anchor_identity(social_url: str, vector_data: list, rpc_url: str, private_key: str, contract_address: str):
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    account = w3.eth.account.from_key(private_key)
    
    # Hash the biometric data to a bytes32 format for Solidity
    vector_hash = hashlib.sha256(str(vector_data).encode()).hexdigest()
    bytes32_hash = Web3.to_bytes(hexstr=vector_hash)

    # Standard ABI for the BiometricRegistry contract
    contract_abi = [{"inputs":[{"internalType":"string","name":"_socialUrl","type":"string"},{"internalType":"bytes32","name":"_faceVectorHash","type":"bytes32"}],"name":"registerIdentity","outputs":[],"stateMutability":"nonpayable","type":"function"}]
    
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)
    
    tx = contract.functions.registerIdentity(social_url, bytes32_hash).build_transaction({
        'from': account.address,
        'nonce': w3.eth.get_transaction_count(account.address),
        'gas': 200000,
        'gasPrice': w3.eth.gas_price
    })
    
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    
    return receipt.transactionHash.hex()
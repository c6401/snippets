from web3 import Web3, HTTPProvider
from eth_account import Account

w3 = Web3(HTTPProvider('https://cloudflare-eth.com/'))
Account.enable_unaudited_hdwallet_features()
acc = Account.from_mnemonic(...)

w3.eth.get_balance(acc.address)
signed = w3.eth.account.sign_transaction({
    'chainId': 1,
    'from': acc.address,
    'to': w3.to_checksum_address(...),
    'value': w3.to_wei(..., 'ether'),
    "gas": 21000,
    "gasPrice": w3.eth.gas_price,
    "nonce": w3.eth.get_transaction_count(acc.address),
}, acc._private_key.hex())

sent = w3.eth.send_raw_transaction(signed.rawTransaction)
result = w3.eth.wait_for_transaction_receipt(sent)

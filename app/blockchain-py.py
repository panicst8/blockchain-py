""" blockchain research """
import hashlib
import json
from time import time
from typing import Any, List


class Blockchain(object):
    """ blockchain main class """

    def __init__(self) -> None:
        self.chain: List[Any] = []
        self.pending_transactions: List[Any] = []

        self.new_block(
            previous_hash="The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.",
            proof=100,
        )

    # Create a new block listing key/value pairs of block information in a JSON object. Reset the list of pending transactions & append the newest block to the chain.

    def new_block(self, proof: Any, previous_hash: Any = None) -> Any:
        """ New Block """
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time(),
            "transactions": self.pending_transactions,
            "proof": proof,
            "previous_hash": previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block

    # Search the blockchain for the most recent block.

    @property
    def last_block(self) -> Any:
        """ return last block """

        return self.chain[-1]

    # Add a transaction with relevant info to the 'blockpool' - list of pending tx's.

    def new_transaction(self, sender: Any, recipient: Any, amount: Any) -> Any:
        """ New Transction """
        transaction = {"sender": sender, "recipient": recipient, "amount": amount}
        self.pending_transactions.append(transaction)
        return self.last_block["index"] + 1

    # receive one block. Turn it into a string, turn that into Unicode (for hashing). Hash with SHA256 encryption, then translate the Unicode into a hexidecimal string.

    def hash(self, block: Any) -> Any:
        """ Hash """
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash


blockchain = Blockchain()
t1 = blockchain.new_transaction("Satoshi", "Mike", "5 BTC")
t2 = blockchain.new_transaction("Mike", "Satoshi", "1 BTC")
t3 = blockchain.new_transaction("Satoshi", "Hal Finney", "5 BTC")
blockchain.new_block(12345)

t4 = blockchain.new_transaction("Mike", "Alice", "1 BTC")
t5 = blockchain.new_transaction("Alice", "Bob", "0.5 BTC")
t6 = blockchain.new_transaction("Bob", "Mike", "0.5 BTC")
blockchain.new_block(6789)

print("Genesis block: ", blockchain.chain)

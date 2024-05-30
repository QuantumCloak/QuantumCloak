#implementing functionalities
from block import Block

class Blockchain:
    def _init_(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2

    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block")

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
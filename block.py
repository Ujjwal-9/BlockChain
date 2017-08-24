class Block:
    def __init__(self,index, previousHash, timestamp, data, hash):
        self.index = index
        self.previousHash = str(previousHash)
        self.timestamp = timestamp
        self.data = data
        self.hash = str(hash)
 

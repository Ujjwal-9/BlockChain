# Hashlib is another library i can use. Now have to check which one is fast.

from Crypto.Hash import SHA256
def calculateHash(index, previousHash, timestamp, data):
	b = bytearray()
	s = index + previousHash + timestamp + data
	h = SHA256.new(b.extend(s.encode()))
    return str(h.hexdigest())
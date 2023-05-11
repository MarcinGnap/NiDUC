import random
class RandomBitsGenerator:
    def __init__(self, numBits):
        self.numBits = numBits

    def generateBits(self):
        return [random.choice([0, 1]) for _ in range(self.numBits)]
class NumberGuess:
    def __init__(self, low, high):
        self.lo = low
        self.hi = high

    def guess(self):
        return (self.lo + self.hi)//2

    def high(self):
        self.hi = (self.lo + self.hi) //2

    def low(self):
        self.lo = (self.lo + self.hi) //2

    def correct(self):
        pass

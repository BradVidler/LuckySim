class Symbol:

    def __init__(self, name, odds, pay5, pay4, pay3, pay2):
        self.name = name
        self.odds = odds
        self.pay5 = pay5
        self.pay4 = pay4
        self.pay3 = pay3
        self.pay2 = pay2

    def getprize(self, count):
        if count == 5:
            return self.pay5
        elif count == 4:
            return self.pay4
        elif count == 3:
            return self.pay3
        elif count == 2:
            return self.pay2
        else:
            return 0

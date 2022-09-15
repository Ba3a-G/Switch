from collections import deque

class Switch():
    """An algorithm that changes base of a number (currently supports only integers and upto base 85)."""

    def __init__(self):
        self.charSet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%&()_+{}|:<>?[]\;/~"

    def divide(self, number: int, base: int) -> int:
        return number // base, number % base

    def symbolTable(self, base: int) -> dict:
        table = {}
        for n in range(base)[10:]:
            table[self.charSet[n]] = n
        return table

    def sanitizeRemainders(self, rems: list) -> list:
        formatted = ""
        for i in range(len(rems)):
            if rems[i] >= 10:
                rems[i] = self.charSet[rems[i]]
            rems[i] = str(rems[i])
            formatted += rems[i]
        return formatted 

    def switch(self, number: int, base: int):
        "Converts the given number to the specified base."
        
        if base >= 85:
            raise Exception('Base greater than 85 not supported, yet.')

        symbolTableRequired = False
        remainders = deque()
        quo = number
        while True:
            quo, rem = self.divide(quo, base)
            remainders.appendleft(rem)
            if quo == 0:
                break
        remainders = list(remainders)
        if base >= 10:
            symbolTable = self.symbolTable(base)
            symbolTableRequired = True
        result = self.sanitizeRemainders(remainders)
        if symbolTableRequired:
            return [result, symbolTable]
        else:
            return [result]

    def toBinary(self, number: int) -> str:
        "Converts the given number to Binary."
        return self.switch(number, 2)[0]

    def toHexadecimal(self, number: int) -> list:
        "Converts the given number to Hexadecimal."
        return self.switch(number, 16)

    def toOctal(self, number: int) -> str:
        "Converts the given number to Octal."
        return self.switch(number, 8)[0]
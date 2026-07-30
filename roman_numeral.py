

class RomanNumber:
    def __init__(self, number):
        self.number = number

    def to_roman(self):
        # Mapping of values to Roman numerals
        val = [1000, 900, 500, 400,
               100, 90, 50, 40,
               10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD",
                "C", "XC", "L", "XL",
                "X", "IX", "V", "IV", "I"]

        num = self.number
        roman = ""

        # Loop through values and symbols
        for i in range(len(val)):
            while num >= val[i]:
                roman += syms[i]
                num -= val[i]

        return roman

    def __str__(self):
        return f"{self.number} → {self.to_roman()}"


# Example usage
print(RomanNumber(124))   # Output: 124 → CXXIV
print(RomanNumber(2567))  # Output: 2567 → MMDLXVII
print(RomanNumber(4))     # Output: 4 → IV

import random


class Password:
    # lists containing the ASCII num ranges for their character categories
    _fullcharlist = [[97, 122], [65, 90], [35, 38], [48, 57]]

    # In the constructor the number of characters of each type is prompted
    def __init__(self, lowercase_letters=1, uppercase_letters=1, symbols=1, numbers=1):
        self.lowercase_letters = lowercase_letters
        self.uppercase_letters = uppercase_letters
        self.symbols = symbols
        self.numbers = numbers
        self.plaintext = ""
        self.charnums = [self.lowercase_letters, self.uppercase_letters, self.symbols, self.numbers]

    # getters/setters
    def get_lowercase(self):
        return self.lowercase_letters

    def get_uppercase(self):
        return self.uppercase_letters

    def get_symbols(self):
        return self.symbols

    def get_numbers(self):
        return self.numbers

    def get_characternums(self):
        return self.charnums

    def get_plaintext(self):
        return self.plaintext

    def set_lowercase(self, num):
        self.lowercase_letters = num

    def set_uppercase(self, num):
        self.uppercase_letters = num

    def set_symbols(self, num):
        self.symbols = num

    def set_numbers(self, num):
        self.numbers = num

    # This function is meant to accept a list and update the charnums list
    def set_characternums(self, lowercase_letters=1, uppercase_letters=1, symbols=1, numbers=1):
        self.charnums = [lowercase_letters, uppercase_letters, symbols, numbers]

    def set_plaintext(self, new_text):
        self.plaintext = new_text

    # methods for password class
    def assemble(self):
        count = 0
        for i in range(len(self._fullcharlist)):
            plaintext_tokens = random.sample(range(self._fullcharlist[i][0], self._fullcharlist[i][1]),
                                             k=self.charnums[count])
            count += 1
            for num in plaintext_tokens:
                self.plaintext += chr(num)
        return

    def scramble(self):
        self.assemble()
        password_tokens = random.sample(self.plaintext, len(self.plaintext))
        scrambled_password = "".join(password_tokens)
        return scrambled_password


if __name__ == "__main__":
    secure_password = Password(2, 3, 1, 6)
    print(secure_password.scramble())

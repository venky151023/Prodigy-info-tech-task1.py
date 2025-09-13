class DecryptEncrypt:
    def text(self):
        pass


class CaesarCipher(DecryptEncrypt):
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, text):
        return self._shift_text(text, self.shift)

    def decrypt(self, text):
        return self._shift_text(text, -self.shift)

    def _shift_text(self, text, shift_amount):
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - base + shift_amount) % 26 + base
                result += chr(shifted)
            else:
                result += char
        return result


def main():
    
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (integer): "))
    mode = input("Choose mode - 'encrypt' or 'decrypt': ").strip().lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
        return

    cipher = CaesarCipher(shift)

    if mode == 'encrypt':
        result = cipher.encrypt(message)
    else:
        result = cipher.decrypt(message)

    print(f"Resulting text ({mode}ed): {result}")


if __name__ == "__main__":

    main()

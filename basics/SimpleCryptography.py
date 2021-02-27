

class Cipher():

    def __init__(self, shift):

        self.encoder = [None]*26
        self.decoder = [None]*26

        for i in range(26):
            self.encoder[i] = chr((i + shift) % 26 + ord('A'))
            self.decoder[i] = chr((i - shift) % 26 + ord('A'))

    def encrypt(self, msg):
        enc_msg = []
        for c in msg:
            if c.isupper():
                pos = ord(c) - ord('A')
                enc_msg.append(self.encoder[pos])
            else:
                enc_msg.append(c)
        return "".join(enc_msg)

    def decrypt(self, msg):
        dec_msg = []
        for c in msg:
            if c.isupper():
                pos = ord(c) - ord('A')
                dec_msg.append(self.decoder[pos])
            else:
                dec_msg.append(c)
        return "".join(dec_msg)


if __name__ == '__main__':
    c = Cipher(5)
    print("Enc")
    print(c.encrypt("HELLO WORLD"))
    print("Dec")
    print(c.decrypt("MJQQT BTWQI"))

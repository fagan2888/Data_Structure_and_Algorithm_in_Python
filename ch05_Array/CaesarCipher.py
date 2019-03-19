class CaesarCipher:
    def __init__(self, shift):
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self, message):
        return self._transform(message, self._forward)

    def decrypt(self, message):
        return self._transform(message, self._backward)

    def _transform(self, orignal, code):
        msg = list(orignal.upper())
        for k in range(len(msg)):
            if msg[k].isalpha():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)

# class CaesarCipher:
#     def __init__(self, shift):
#         self._shift = shift

#     def encrypt(self, message):
#         secret = []
#         for e in message.upper():
#             if e.isalpha():
#                 s, r = divmod(ord(e) + self._shift, ord('Z') + 1)
#                 secret.append(chr(r + s * ord('A')))
#             else:
#                 secret.append(e)
#         return ''.join(secret)

#     def decrypt(self, secret):
#         msg = []
#         for c in secret.upper():
#             if c.isalpha():
#                 s, r = divmod(ord(c) - self._shift, ord('A'))
#                 if s == 0:
#                     msg.append(chr(ord('Z') - ord('A') + r + 1))
#                 else:
#                     msg.append(chr(ord(c) - self._shift))
#             else:
#                 msg.append(c)
#         return ''.join(msg)


if __name__ == "__main__":
    msg = "THE EAGLE IS IN PLAY; MEET AT JOE’S."
    cc = CaesarCipher(3)
    code = cc.encrypt(msg)
    print(code)
    msg_n = cc.decrypt(code)
    print(msg_n)

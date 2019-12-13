def encrypt_caesar(msg, shift = 3):
    msg = msg.split()
    for word, words in enumerate(msg):
        for ix, char in enumerate(words):
            msg[word] = msg[word][:ix] + chr(ord(char) + shift) + msg[word][ix + 1:]
    return ' '.join(msg)


def decrypt_caesar(msg, shift = 3):
    msg = msg.split()
    for word, words in enumerate(msg):
        for ix, char in enumerate(words):
            msg[word] = msg[word][:ix] + chr(ord(char) - shift) + msg[word][ix+1:]
    return ' '.join(msg)


msg = 'Да здравствует салат Цезарь!'
shift = 3
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)
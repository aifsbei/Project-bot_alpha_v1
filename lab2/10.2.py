step = int(input())
msg = input()
new_msg = ''
for letter in msg:
    if letter.isalpha():
        letter = chr(ord(letter) + step)
    new_msg += letter
print(new_msg)
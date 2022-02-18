def Caesar():
    message = input('plain text: ')
    cipherchars = [''for i in range(len(message))]
    key = int(input('please entre the key: '))
    for i in range(len(message)):
        char = message[i]
        cipherchar = ord(char) + key
        cipherchars.append(chr(cipherchar))
    print('cipher text:', ''.join(cipherchars))

Caesar()

# Caesar cipher basic code
text = input("Enter your message: ")
shift = int(input())
cipher = ''
for c in text:
    if not c.isalpha():
        continue
    char = c.upper()
    char = ord(c)
    char = ord(c) - ord("A")
    code = (int(char) + shift)
    code2 = code + ord("A")
    code3 = chr(code2)
    cipher += chr(code2)

print(cipher)

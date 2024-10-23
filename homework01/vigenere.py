def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    mask = [value.isupper() for value in plaintext]
    encrypt_vigenere_text = list(plaintext)  
    keyword = keyword.upper()
    plaintext = plaintext.upper()
    new_keyword = []
    keyword_length = len(keyword)

    for i in range(len(plaintext)):
        if plaintext[i].isalpha():  
            new_keyword.append(keyword[i % keyword_length])  
        else:
            new_keyword.append(None)   

    for i, char in enumerate(plaintext):
        if char.isalpha():
            num_key = (ord(char) - ord('A') + ord(new_keyword[i]) - ord('A')) % 26
            encrypt_char = chr(num_key + ord('A')) 
            encrypt_vigenere_text[i] = encrypt_char if mask[i] else encrypt_char.lower()

    return ''.join(encrypt_vigenere_text)

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    mask = [value.isupper() for value in ciphertext]
    decrypt_vigenere_text = list(ciphertext)
    keyword = keyword.upper()
    ciphertext = ciphertext.upper()
    new_keyword = []
    keyword_length = len(keyword)
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():  
            new_keyword.append(keyword[i % keyword_length])
        else:
            new_keyword.append(None)   

    for i, char in enumerate(ciphertext):
        if char.isalpha(): 
            num_key = (ord(char) - ord(new_keyword[i])) % 26 
            decrypt_char = chr(num_key + ord('A'))  
            decrypt_vigenere_text[i] = decrypt_char if mask[i] else decrypt_char.lower()

    return ''.join(decrypt_vigenere_text)
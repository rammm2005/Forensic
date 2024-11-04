from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def encrypt(text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_text = cipher.encrypt(pad(text.encode(), AES.block_size))
    return iv + encrypted_text

key = get_random_bytes(16)

words = "file3 file4 file6 file5 file1 file2"

encrypted_combined = b"".join(encrypt(word, key) for word in words.split())

print("Encrypted words:")
for word in words.split():
    encrypted = encrypt(word, key)
    print(f"{word} -> {encrypted.hex()}")

print("\nCombined encrypted data:")
print(encrypted_combined.hex())

with open("encrypted_data.bin", "wb") as f:
    f.write(encrypted_combined)  

with open("key.bin", "wb") as f:
    f.write(key)

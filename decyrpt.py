from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt(encrypted_data, key):
    iv = encrypted_data[:AES.block_size] 
    encrypted_text = encrypted_data[AES.block_size:]  
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    try:
        decrypted_text = unpad(cipher.decrypt(encrypted_text), AES.block_size)
        return decrypted_text.decode('utf-8')  
    except ValueError as e:
        print(f"Error during unpadding: {e}")
        return None
    except Exception as e:
        print(f"Error decrypting data: {e}")
        return None

with open("key.bin", "rb") as f:
    key = f.read()

with open("encrypted_data.bin", "rb") as f:
    encrypted_data = f.read()

decrypted_words = ""
offset = 0

while offset < len(encrypted_data):
    if offset + AES.block_size > len(encrypted_data):
        print("Not enough data to read IV. Exiting.")
        break

    iv = encrypted_data[offset:offset + AES.block_size] 
    offset += AES.block_size

    remaining_length = len(encrypted_data) - offset

    if remaining_length < AES.block_size:
        print("Not enough data to read the encrypted text. Exiting.")
        break  

    encrypted_text = encrypted_data[offset:offset + AES.block_size]

    decrypted_word = decrypt(iv + encrypted_text, key)
    if decrypted_word is not None:
        decrypted_words += decrypted_word + " " 
    else:
        break  

    offset += AES.block_size

print("\nDecrypted words:")
print(decrypted_words.strip()) 

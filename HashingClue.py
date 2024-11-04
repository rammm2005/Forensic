import hashlib

def encrypt_repeatedly(text, times):
    for _ in range(times):
        text = hashlib.sha256(text.encode()).hexdigest()
    return text

words = ["file3", "file4", "file6", "file5", "file1", "file2"]

encrypted_words = [encrypt_repeatedly(word, 3) for word in words]
combined_encrypted = ''.join(encrypted_words)

final_hash = hashlib.sha256(combined_encrypted.encode()).hexdigest()

print(f"Final hash gabungan: {final_hash}")

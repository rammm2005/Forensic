import binascii

def decode_password_part(encoded_part):
    """Mendekode bagian password yang di-encode dengan Hexadecimal."""
    return binascii.unhexlify(encoded_part).decode('utf-8')

def main():
    encoded_input = input("Masukkan bagian password yang telah di-encode (Hexadecimal): ")

    try:
        decoded_part = decode_password_part(encoded_input)
        print("Bagian password asli:", decoded_part)
    except Exception as e:
        print("Terjadi kesalahan saat mendekode:", str(e))

if __name__ == "__main__":
    main()

import base64

encrypted_password_part = base64.b64encode("hari".encode()).decode()

def get_password_part():
    print("Jika dua angka berurutan ditambahkan menghasilkan 21, berapakah angka yang lebih kecil?")
    
    answer = input("Jawaban Anda: ")
    
    if answer == "10":
        return base64.b64decode(encrypted_password_part).decode()
    else:
        print("Jawaban salah. Coba lagi!")
        return None

if __name__ == "__main__":
    part = get_password_part()
    if part:
        print("Bagian password:", part)
    else:
        print("Gagal mendapatkan bagian password.")

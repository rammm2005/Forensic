import base64

encrypted_password_part = base64.b64encode("ss".encode()).decode()

def get_password_part():
    print("Deret berikut adalah 3, 9, 27, 81, ..., berapa angka ke-6 dalam deret ini?")
    
    answer = input("Jawaban Anda: ")
    
    if answer == "729":
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

import base64

encrypted_password_part = base64.b64encode("23".encode()).decode()

def get_password_part():
    print("Jika sebuah angka bulat habis dibagi 12 dan 18, berapa angka bulat positif terkecil yang memenuhi kondisi ini?")
    
    answer = input("Jawaban Anda: ")
    
    if answer == "36":
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

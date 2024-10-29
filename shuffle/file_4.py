import base64

encrypted_password_part = base64.b64encode("rd".encode()).decode()

def get_password_part():
    print("Algoritma hash apa yang memiliki panjang output 160-bit dan sering digunakan untuk memverifikasi integritas data di IT Forensik?")
    
    answer = input("Jawaban Anda: ")
    
    if answer.lower() == "sha-1":
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

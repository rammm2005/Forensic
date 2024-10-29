import base64
import getpass

encrypted_password_part = base64.b64encode("xy".encode()).decode()

def get_password_part():
    print("Dalam investigasi forensik, teknik apa yang sering digunakan untuk menyembunyikan")
    print("data dalam file atau jaringan tanpa terlihat, dengan cara mengombinasikan algoritma")
    print("kriptografi simetris dalam mode stream cipher yang diimplementasikan dengan XOR")
    print("terhadap data mentah? (Masukkan nama metode yang tepat)")

    answer = getpass.getpass("Jawaban Anda: ")

    if answer.lower() == "steganography":
        print("Jawaban benar!")
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

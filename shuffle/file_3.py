import base64

encrypted_password_part = base64.b64encode("wo".encode()).decode()

def get_password_part():
    print("Protokol apa yang digunakan untuk menangkap bit mentah dalam forensik jaringan,")
    print("sering diimplementasikan sebagai alat untuk merekam trafik yang beredar pada Layer OSI ke-3 (jawaban more than 1 😄)?")
    
    answer = input("Jawaban Anda: ")
    
    if answer.lower() in ["pcap", "tcpdump", "wireshark", "libpcap"]:
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

import PyPDF2

def encrypt_pdf(input_pdf_path, output_pdf_path, password):
    with open(input_pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()
        
        for page in reader.pages:
            writer.add_page(page)
        
        writer.encrypt(password)

        with open(output_pdf_path, "wb") as output_file:
            writer.write(output_file)
    
    print(f"PDF file encrypted and saved as: {output_pdf_path}")

def main():
    input_pdf = input("Masukkan path file PDF yang ingin dienkripsi: ")
    output_pdf = input("Masukkan path untuk menyimpan PDF yang dienkripsi: ")
    password = input("Masukkan password untuk enkripsi: ")
    
    encrypt_pdf(input_pdf, output_pdf, password)

if __name__ == "__main__":
    main()

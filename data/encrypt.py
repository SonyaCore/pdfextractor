from data.pdf import *
writer = PdfWriter()

def encrypt_pdf(name,password):
        """encrypt pdf with password"""
        try:
            reader = PdfReader(name)

            if not password:
                password='123'

            elif len(str(password)) < 3:
                raise TypeError()

            for page in reader.pages:
                writer.add_page(page)

            writer.encrypt(str(password))

            with open(f"{name}.encrypt", "wb") as encrypted:
                writer.write(encrypted)
        except TypeError:
            print('weak password')
            exit()
    
def decrypt_pdf(name,password):
        """decrypt pdf with password"""
        try:
            reader = PdfReader(name)
            output = str(f"decrypted.{name}".replace('.encrypt', ''))

            if reader.is_encrypted:
                reader.decrypt(password)

            for page in reader.pages:
                writer.add_page(page)

            with open(f"{output}", "wb") as decrypted:
                writer.write(decrypted)

        except PyPDF2.errors.PdfReadError:
            print('Incorrect Password')
            exit()
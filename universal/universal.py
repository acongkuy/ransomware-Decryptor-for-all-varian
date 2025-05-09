import os
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import unpad
import base64

# ASCII Art - UNIVERSAL
print("""
  U   U  N   N  III  V   V  EEEEE  RRRR    SSSS   AAAAA  L
  U   U  NN  N   I   V   V  E      R   R  S       A   A  L
  U   U  N N N   I   V   V  EEEE   RRRR   SSSS    AAAAA  L
  U   U  N  NN   I   V   V  E      R  R       S   A   A  L
  UUUU   N   N  III   VVV   EEEEE  R   R  SSSS    A   A  LLLLL
""")

def detect_encryption_algorithm(file_path):
    """ Mendeteksi algoritma enkripsi yang digunakan """
    with open(file_path, 'rb') as file:
        data = file.read(64)  # Baca bagian pertama dari file terenkripsi
        # Cek jika file terenkripsi dengan AES
        if data.startswith(b'Encrypted with AES'):
            return 'AES'
        # Cek jika file terenkripsi dengan RSA
        elif data.startswith(b'Encrypted with RSA'):
            return 'RSA'
        # Tambahkan lebih banyak pengecekan sesuai dengan algoritma lain
        else:
            return 'Unknown'

def decrypt_aes(file_path, key, output_path):
    """ Dekripsi menggunakan AES """
    with open(file_path, 'rb') as enc_file:
        encrypted_data = enc_file.read()
    
    iv = encrypted_data[:16]  # Ambil IV dari bagian pertama file
    encrypted_data = encrypted_data[16:]  # Sisa data terenkripsi
    
    key = hashlib.sha256(key.encode('utf-8')).digest()  # Ubah key menjadi 32 byte
    cipher = AES.new(key, AES.MODE_CBC, iv)  # Inisialisasi cipher AES
    
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)  # Dekripsi
    
    with open(output_path, 'wb') as dec_file:
        dec_file.write(decrypted_data)
    
    print(f"Decryption complete! The decrypted file is saved at: {output_path}")

def decrypt_rsa(file_path, private_key_path, output_path):
    """ Dekripsi menggunakan RSA """
    with open(file_path, 'rb') as enc_file:
        encrypted_data = enc_file.read()
    
    with open(private_key_path, 'rb') as priv_key_file:
        private_key = RSA.import_key(priv_key_file.read())
        cipher_rsa = PKCS1_OAEP.new(private_key)
    
    decrypted_data = cipher_rsa.decrypt(encrypted_data)  # Dekripsi data
    
    with open(output_path, 'wb') as dec_file:
        dec_file.write(decrypted_data)
    
    print(f"Decryption complete! The decrypted file is saved at: {output_path}")

def main():
    file_path = input("Enter the path of the encrypted file: ").strip()
    output_path = input("Enter the path to save the decrypted file: ").strip()
    key = input("Enter the decryption key (for AES only): ").strip()
    private_key_path = input("Enter the private key file path (for RSA only): ").strip()

    encryption_algorithm = detect_encryption_algorithm(file_path)
    
    if encryption_algorithm == 'AES':
        decrypt_aes(file_path, key, output_path)
    elif encryption_algorithm == 'RSA':
        decrypt_rsa(file_path, private_key_path, output_path)
    else:
        print("Unknown encryption algorithm or unsupported algorithm.")

if __name__ == "__main__":
    main()


# Universal Decryptor - All-in-One Ransomware Decryptor

**Universal Decryptor** adalah alat yang dirancang untuk mendekripsi file yang terenkripsi oleh ransomware. Alat ini dapat mendeteksi dan menangani beberapa varian ransomware, seperti yang menggunakan **AES** (Advanced Encryption Standard) dan **RSA** (Rivest-Shamir-Adleman). Program ini dilengkapi dengan antarmuka berbasis teks (CLI) dan menampilkan **ASCII Art** yang menarik di bagian atas.

---

## **Fitur**:

* Mendeteksi algoritma enkripsi (AES, RSA).
* Mendekripsi file terenkripsi dengan **AES** atau **RSA**.
* **Mudah digunakan** dengan antarmuka berbasis CLI.
* **Kompatibel dengan Windows, Linux, dan macOS**.
* **ASCII Art "UNIVERSAL"** yang menarik di awal.

---

## **Prasyarat**:

Sebelum mulai, pastikan kamu memiliki:

* **Python 3.6+** terinstal di sistem kamu.
* **pip** untuk mengelola paket Python.
* **pycryptodome** untuk enkripsi dan dekripsi.

---

## **Instalasi**:

### **1. Instal Python dan pip**:

Jika kamu belum memiliki **Python** atau **pip** terinstal, berikut adalah cara untuk menginstalnya:

* **Linux (Ubuntu/Debian)**:

  ```bash
  sudo apt update
  sudo apt install python3 python3-pip
  ```

* **macOS**:
  Install Homebrew terlebih dahulu jika belum ada:

  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  brew install python
  ```

* **Windows**:
  Unduh dan instal Python 3 dari [python.org](https://www.python.org/downloads/), pastikan untuk memilih opsi **Add Python to PATH** saat instalasi.

---

### **2. Membuat Virtual Environment (Opsional)**:

Untuk memastikan instalasi yang terisolasi, sangat disarankan untuk menggunakan **virtual environment**.

1. **Instal `python3-venv`** (jika belum terpasang):

   * **Linux (Ubuntu/Debian)**:

     ```bash
     sudo apt install python3-venv
     ```
   * **macOS** dan **Windows**: Virtual environment sudah terinstal secara default di Python 3.

2. **Buat Virtual Environment**:
   Di direktori proyek kamu, jalankan:

   ```bash
   python3 -m venv universal-decryptor-env
   ```

3. **Aktifkan Virtual Environment**:

   * **Linux/macOS**:

     ```bash
     source universal-decryptor-env/bin/activate
     ```
   * **Windows**:

     ```bash
     universal-decryptor-env\Scripts\activate
     ```

4. **Instal dependensi**:
   Setelah virtual environment aktif, instal **pycryptodome** dengan:

   ```bash
   pip install pycryptodome
   ```

---

### **3. Mengunduh dan Menjalankan Universal Decryptor**:

1. **Clone Repository**:
   Jika kamu belum meng-clone repository ini, lakukan dengan perintah berikut:

   ```bash
   git clone https://github.com/acongkuy/ransomware-Decryptor-for-all-varian
   cd universal
   ```

2. **Jalankan Universal Decryptor**:
   Setelah berada di dalam direktori proyek, jalankan alat dekripsi dengan perintah:

   ```bash
   python universal.py
   ```

---

## **Penggunaan**:

Setelah menjalankan perintah di atas, kamu akan diminta untuk memberikan input sebagai berikut:

1. **Enter the path of the encrypted file**:

   * Masukkan **path lengkap** ke **file terenkripsi** yang ingin kamu dekripsi.
   * Misalnya: `/path/to/encrypted/file` (Linux/macOS) atau `C:\Users\Username\Downloads\encrypted_file.txt` (Windows).

2. **Enter the path to save the decrypted file**:

   * Masukkan **path lengkap** untuk **menyimpan file yang didekripsi**.
   * Misalnya: `/path/to/decrypted/file` (Linux/macOS) atau `C:\Users\Username\Downloads\decrypted_file.txt` (Windows).

3. **Enter the decryption key**:

   * Masukkan **kunci dekripsi** yang digunakan saat ransomware mengenkripsi file. (Hanya diperlukan untuk **AES**).

4. **Enter the private key file path**:

   * Masukkan **path ke file kunci pribadi RSA** (Hanya diperlukan untuk **RSA**).

Contoh output:

```bash
  U   U  N   N  III  V   V  EEEEE  RRRR    SSSS   AAAAA  L
  U   U  NN  N   I   V   V  E      R   R  S       A   A  L
  U   U  N N N   I   V   V  EEEE   RRRR   SSSS    AAAAA  L
  U   U  N  NN   I   V   V  E      R  R       S   A   A  L
  UUUU   N   N  III   VVV   EEEEE  R   R  SSSS    A   A  LLLLL

Enter the path of the encrypted file: /path/to/encrypted/file
Enter the path to save the decrypted file: /path/to/decrypted/file
Enter the decryption key (for AES only): my_decryption_key
Enter the private key file path (for RSA only): /path/to/private_key.pem

Decryption complete! The decrypted file is saved at: /path/to/decrypted/file
```

---

## **FAQ (Pertanyaan yang Sering Diajukan)**

### **Q1: Apa itu Universal Decryptor?**

Universal Decryptor adalah alat untuk mendekripsi file yang terenkripsi oleh ransomware yang menggunakan algoritma **AES** atau **RSA**.

### **Q2: Bagaimana jika kunci dekripsi saya salah?**

Jika kunci dekripsi salah, dekripsi akan gagal dan pesan kesalahan akan ditampilkan.

### **Q3: Apakah Universal Decryptor bekerja di semua sistem operasi?**

Universal Decryptor bekerja di **Linux**, **macOS**, dan **Windows** asalkan **Python 3.6+** terinstal.

---

## **Menyumbang**:

Jika kamu ingin menyumbang ke pengembangan Universal Decryptor, fork repo ini dan buat pull request dengan perubahan yang diinginkan. Kami menyambut kontribusi dan perbaikan bug.

---

**Terima kasih telah menggunakan Universal Decryptor!**

---

### **Kesimpulan**:

Ini adalah tutorial lengkap untuk membuat **tools Universal Decryptor** di CLI, termasuk cara instalasi dan penggunaannya. Semua langkah ini dioptimalkan untuk lingkungan yang bersih menggunakan **virtual environment** agar menghindari konflik dengan sistem Python yang sudah ada.

Jika ada pertanyaan lebih lanjut atau masalah dengan penggunaan tools, silakan beri tahu saya!

---

Ini adalah **README** yang sudah lengkap dengan penjelasan cara menggunakan alat **Universal Decryptor**. Jika ada tambahan atau perubahan lain yang diinginkan, beri tahu saya!


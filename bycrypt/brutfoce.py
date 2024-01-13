

import bcrypt

def check_password(password, given_hash):
    """Membandingkan password dengan hash bcrypt yang diberikan."""
    return bcrypt.checkpw(password.encode(), given_hash.encode())

# wordlist = ['123456', 'kata2', 'kata3', 'kata4', 'kata5']  # Ganti dengan kata-kata yang ingin Anda coba
wordlist = [
    "password",
    "123456",
    "qwerty",
    "abc123",
    "nama",
    "namadepan",
    "namabelakang",
    "tanggallahir",
    "tempatlahir",
    "kotalahir",
    "alamat",
    "nomortelepon",
    "email",
    "username",
    "katakataindonesia",
    "katakatainggris",
    "katakatabahasalain",
]

hash_to_crack = "$2y$10$MzZJl1fM/Bfy72eNgZ1Ju.r9CUXvW0WGgIO2kYoRjk/S/3hIZoyfC"

password_found = False
for word in wordlist:
    if check_password(word, hash_to_crack):
        print(f"Password found: {word}")
        password_found = True
        break

if not password_found:
    print("Password tidak ditemukan dalam wordlist.")

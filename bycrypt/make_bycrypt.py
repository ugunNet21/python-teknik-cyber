import bcrypt

# Mendefinisikan kata sandi
# password_to_hash = "my_secure_password"
password_to_hash = "ugun"

# Menghasilkan salt (garam) secara otomatis
salt = bcrypt.gensalt()

# Menggunakan bcrypt untuk mengenkripsi kata sandi dengan salt
hashed_password = bcrypt.hashpw(password_to_hash.encode('utf-8'), salt)

# Menampilkan hasil
print(f"Password: {password_to_hash}")
print(f"Salt: {salt}")
print(f"Hashed Password: {hashed_password}")


# PS D:\web\decrypt\bycrypt> python .\make_bycrypt.py
# Password: my_secure_password
# Salt: b'$2b$12$iRfohHLuaKwHpdmFAIN7c.'
# Hashed Password: b'$2b$12$iRfohHLuaKwHpdmFAIN7c.0Y4BuTavQ2L9hiuHpggrEHF8aDV2iMG'
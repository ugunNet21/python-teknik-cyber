import bcrypt

# Mendefinisikan kata sandi
password_to_hash = "my_secure_password"

# Menghasilkan salt (garam) secara otomatis
salt = bcrypt.gensalt()

# Menggunakan bcrypt untuk mengenkripsi kata sandi dengan salt
hashed_password = bcrypt.hashpw(password_to_hash.encode('utf-8'), salt)

# Menampilkan hasil
print(f"Password: {password_to_hash}")
print(f"Salt: {salt}")
print(f"Hashed Password: {hashed_password}")

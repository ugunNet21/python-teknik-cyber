import bcrypt

# Hash yang diberikan
hashed_password = "$2y$10$MzZJl1fM/Bfy72eNgZ1Ju.r9CUXvW0WGgIO2kYoRjk/S/3hIZoyfC"

# Kata sandi untuk memverifikasi
password_to_check = "123456"

# Memverifikasi kata sandi
if bcrypt.checkpw(password_to_check.encode('utf-8'), hashed_password.encode('utf-8')):
    print("Password Benar!")
else:
    print("Password Salah.")

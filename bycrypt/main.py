import bcrypt

def decrypt_password(hash_password):
    # Buat objek bcrypt
    bcrypt = bcrypt.hashpw("password", bcrypt.gensalt(10))

    # Dekripsi hash password
    return bcrypt.decrypt(hash_password)


if name == "main":
    hash_password = "$2y$10$MzZJl1fM/Bfy72eNgZ1Ju.r9CUXvW0WGgIO2kYoRjk/S/3hIZoyfC"
    password = decrypt_password(hash_password)
    print(password)

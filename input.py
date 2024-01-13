import bcrypt

def check_password(hash_password, plain_password):
    # Periksa apakah plain_password cocok dengan hash_password
    return bcrypt.checkpw(plain_password.encode(), hash_password.encode())


if __name__ == "__main__":
    hash_password = "$2y$10$MzZJl1fM/Bfy72eNgZ1Ju.r9CUXvW0WGgIO2kYoRjk/S/3hIZoyfC"
    password_to_check = input("Masukkan password: ")  # Minta masukan password

    if check_password(hash_password, password_to_check):
        print("Password cocok!")
    else:
        print("Password tidak cocok!")

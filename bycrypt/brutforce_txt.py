import bcrypt

def check_password(password, given_hash):
    """Membandingkan password dengan hash bcrypt yang diberikan."""
    return bcrypt.checkpw(password.encode(), given_hash.encode())

with open("world_list.txt", "r") as file:
    wordlist = file.readlines()

hash_to_crack = "$2y$10$MzZJl1fM/Bfy72eNgZ1Ju.r9CUXvW0WGgIO2kYoRjk/S/3hIZoyfC"

password_found = False
for word in wordlist:
    word = word.strip()
    if check_password(word, hash_to_crack):
        print(f"Password found: {word}")
        password_found = True
        break

if not password_found:
    print("Password tidak ditemukan dalam wordlist.")

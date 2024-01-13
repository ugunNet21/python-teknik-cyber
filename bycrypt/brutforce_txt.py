import bcrypt

def check_password(password, given_hash):
    """Membandingkan password dengan hash bcrypt yang diberikan."""
    return bcrypt.checkpw(password.encode(), given_hash.encode())

with open("world_list.txt", "r") as file:
    wordlist = file.readlines()

hash_to_crack = "$2y$10$MzZJl1fM/Bfy72eNgZ1Ju.r9CUXvW0WGgIO2kYoRjk/S/3hIZoyfC"
# hash_to_crack = "$2b$12$4yvc.xrfUg556kdvsPQEluE6O9jan/M0YyHwJeP8.HdNJnIGlNkiC"
# hash_to_crack = "$2b$12$X0Wfi6Te1ySM1Uts0A5/Q.ZF31vAaYOTPSEiDQANaSqzo.0OJ0xw2"
# hash_to_crack = "$2b$12$mFjPKUg4Gr9ilD9hwVGIF.Ha8sEKVPyumidXIQMcoXkSCml2y43Uq"
# hash_to_crack = "$2y$10$1Z7U1aA5YEcRXnBDtIjtx.7vVTlWW.YQ1YqArQlsky.MucV79rhFu"
# hash_to_crack = "$2b$12$fcht37GhmU.5fEyCv34jZe74jJVw7537hmaCr5s7aDm3iYeiIgN92"
# hash_to_crack = "$2y$10$dVwFtsHMSQ/l1WapGgbi1uRklHOgliS5YT.YCitp/bm1s5Z9RhRI."

password_found = False
for word in wordlist:
    word = word.strip()
    if check_password(word, hash_to_crack):
        print(f"Password found: {word}")
        password_found = True
        break

if not password_found:
    print("Password tidak ditemukan dalam wordlist.")

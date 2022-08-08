from cryptography.fernet import Fernet

key = Fernet.generate_key()
file = open("EncKey.txt", "wb")
file.write(key)
file.close()
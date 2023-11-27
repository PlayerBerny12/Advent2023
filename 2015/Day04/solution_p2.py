import hashlib

key = "ckczppom"

i = 0
while True:
    hash = hashlib.md5(f"{key}{i}".encode())
    if hash.hexdigest().startswith("000000") :
        break
    i += 1

print(i)
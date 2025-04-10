import hashlib
import os

def hash_file(filename):
    with open(filename, 'rb') as f:
        contents = f.read()
        return hashlib.sha256(contents).hexdigest()

def store_hash(filename):
    hashed = hash_file(filename)
    with open("stored.txt", 'w') as f:
        f.write(hashed)
    print(" File hash stored.")

def check_integrity(filename):
    current_hash = hash_file(filename)

    try:
        with open("stored.txt", 'r') as f:
            stored_hash = f.read().strip()

        if current_hash == stored_hash:
            print(" File has not been changed.")
        else:
            print("File has been modified!")
    except FileNotFoundError:
        print(" No stored hash found.")

filename = input("Enter the filename to check or store: ")

if os.path.exists("stored.txt"):
    check_integrity(filename)
else:
    store_hash(filename)


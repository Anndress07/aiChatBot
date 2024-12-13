import bcrypt

import bcrypt

# example password
password = 'rolerskateswithoutl'

# converting password to array of bytes
bytes = password.encode('utf-8')

# generating the salt
salt = bcrypt.gensalt()

# Hashing the password
hash = bcrypt.hashpw(bytes, salt)

print(hash)
print(len(hash))
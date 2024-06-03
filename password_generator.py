# password generator
# This application we would generate a password on different complexity
import string
import random
character = string.ascii_letters+string.digits+string.punctuation
password="".join(random.choice(character)for x in range(8,16))
print(password)
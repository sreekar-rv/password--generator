import random
import array

# Maximum length of the password needed
# You can change this to suit your desired password length
MAX_LEN = 12

# Define character arrays to use in the password
# Represented as strings for easier concatenation
DIGITS = '0123456789'
LOCASE_CHARACTERS = 'abcdefghijklmnopqrstuvwxyz'
UPCASE_CHARACTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SYMBOLS = '@#$%=:?.|~>*()'

# Combine all the character arrays above to form one array
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

# Initialize an empty password string
password = ""

# Ensure we have at least one character from each character set
password += random.choice(DIGITS)      # Add a random digit
password += random.choice(UPCASE_CHARACTERS)  # Add a random uppercase character
password += random.choice(LOCASE_CHARACTERS)  # Add a random lowercase character
password += random.choice(SYMBOLS)     # Add a random symbol

# Fill the remaining password length by selecting randomly from the combined list
for _ in range(MAX_LEN - 4):
    password += random.choice(COMBINED_LIST)

# Convert the password string into an array and shuffle it
password_list = array.array('u', password)
random.shuffle(password_list)

# Convert the shuffled password array back to a string
password = ''.join(password_list)

# Print the generated password
print("Your new Password is: " + password)

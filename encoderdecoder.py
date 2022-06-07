import string

# Creating the letter subsitution for the encoding program
encode_substitution = {i:chr(ord(i)+1) for i in string.ascii_uppercase}
encode_substitution['Z'] = 'A'
encode_substitution[' '] = ' '
decode_substitution = {i:chr(ord(i)-1) for i in string.ascii_uppercase}
decode_substitution['A'] = 'Z'
decode_substitution[' '] = ' '
encode_substitutionl = {i:chr(ord(i)+1) for i in string.ascii_lowercase}
encode_substitutionl['z'] = 'a'
decode_substitutionl = {i:chr(ord(i)-1) for i in string.ascii_lowercase}
decode_substitutionl['a'] = 'z'

encode_substitution.update(encode_substitutionl)
decode_substitution.update(decode_substitutionl)

#print(encode_substitution)
#print(decode_substitution)

# Ask for message
message = input("Enter your message: ")

#Algorithm to encode
def encode(message):
    new_message = ""
    #take each letter and transform it using cipher
    for letter in message:
        new_message += encode_substitution[letter]
    return(new_message)

# Encode the message
encoded_message = encode(message)
#print(encoded_message)

# Take the encoded message and decode it
def decode(encoded_message):
    new_message = ""
    for letter in encoded_message:
        new_message += decode_substitution[letter]
    return(new_message)

decoded_message = decode(encoded_message)
#print(decoded_message)

# Compare final decoded message with the original message
print("Here is your encoded message, ", encoded_message, ", and your decoded message, ", decoded_message, ".")
if message == decoded_message:
    print("Decoded message and message is same.")

import base64

# Encoded message to be decoded
encoded_message = "YS5wLnRoYW5nYW11dGh1"

# Decode the message from base64
decoded_message = base64.b64decode(encoded_message).decode('utf-8')

# Display the results
print("Encoded Message (Base64):", encoded_message)
print("Decoded Message:", decoded_message)

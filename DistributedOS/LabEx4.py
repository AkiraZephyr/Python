import base64
# Message to be encoded
original_message = "Hello, this is a sample message for encoding."

# Encode the message to base64
encoded_message = base64.b64encode(original_message.encode('utf-8')).decode('utf-8')

# Display the results
print("Original Message:", original_message)
print("Encoded Message (Base64):", encoded_message)

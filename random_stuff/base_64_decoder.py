import base64

encoded_str = "cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMWY4MzI2MTV9"
decoded_bytes = base64.b64decode(encoded_str)

# Use 'ignore' to skip any characters that can't be decoded
decoded_str = decoded_bytes.decode('utf-8', errors='ignore')
print(decoded_str)

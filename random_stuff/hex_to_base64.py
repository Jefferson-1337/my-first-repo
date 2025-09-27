import binascii
import base64

# Hexadecimal string
hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

# Convert hex to bytes
bytes_data = binascii.unhexlify(hex_string)

# Convert bytes to base64
base64_data = base64.b64encode(bytes_data)

# Decode base64 bytes to string
base64_string = base64_data.decode('utf-8')

print(base64_string)

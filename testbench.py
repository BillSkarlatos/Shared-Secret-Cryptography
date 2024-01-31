from key_handling import *
from messages_conversions import *
from XOR_Gate import *

def xor_gate(message, key):
    # Convert message and key to binary strings
    binary_msg = ''.join(format(ord(char), '08b') for char in message)
    binary_key = ''.join(format(ord(char), '08b') for char in key)

    # Apply XOR operation for each bit
    result_binary = ''.join('1' if a != b else '0' for a, b in zip(binary_msg, binary_key))

    # Convert binary result back to string
    result_string = ''.join(chr(int(result_binary[i:i+8], 2)) for i in range(0, len(result_binary), 8))

    return result_string

# Sender's perspective
original_message = "Hello, World!"
key = "1433209342009"
encoded_message = xor_gate(original_message, key)

# Receiver's perspective
received_message = xor_gate(encoded_message, key)

print("Original Message:", original_message)
print("Encoded Message:", encoded_message)
print("Decoded Message:", received_message)
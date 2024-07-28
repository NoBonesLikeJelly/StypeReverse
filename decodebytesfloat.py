import struct

# Hexadecimal string
hex_str = '836b5cc2'
hex_str_double = '0b61adb97a71ae35'

# Convert hex string to bytes
byte_data = bytes.fromhex(hex_str)
double_byte_data = bytes.fromhex(hex_str_double)

# Unpack bytes as a 32-bit float
float_value = struct.unpack('f', byte_data)[0]
double_value = struct.unpack('d', double_byte_data)[0]

# Print the result
print("{:.0f}".format(float_value))
#print(double_value)

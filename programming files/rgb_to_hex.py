# Program takes rgb values (respectively) and converts them to hexadecimal binary digits
# which corresponds to a color value on the color wheel

# function rgb_to_hex: turns rgb values to hexadecimal digits
# @param r: scale color with possible input values (0 to 255)
# @param g: scale color with possible input values (0 to 255)
# @param b: scale color with possible input values (0 to 255)
def rgb_to_hex(r, g, b):
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    return '{:02X}{:02X}{:02X}'.format(r, g, b)

# example input
# test with hex_color = rgb_to_hex(255, 127, 0) # returns "FF7F00"

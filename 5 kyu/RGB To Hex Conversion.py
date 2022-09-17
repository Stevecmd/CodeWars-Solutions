def rgb(r, g, b):
    r,g,b = [color if color <= 255 else 255 for color in (r,g,b)] #testing negative/0 values
    r,g,b = [color if color >= 0 else 0 for color in (r,g,b)] #testing near 0 values and above
    return ''.join([hex(color)[2:].upper().zfill(2) for color in (r,g,b)])

print(rgb(255,255,255)) #these are sample values 
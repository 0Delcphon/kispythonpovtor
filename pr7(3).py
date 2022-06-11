def main(x):
    A = x&0b11111111111111
    B = (x >> 14)&0b1111111111111111
    C = (x >> 30)&0b1
    D = (x >> 31)&0b1


    fake = 0
    fake |= D
    fake |= A << 1
    fake |= B << 15
    fake |= C << 31

    return fake


print(hex(main(0x20f78f5e)))
print(hex(main(0x4e61925e)))
print(hex(main(0x717274b1)))
print(hex(main(0x262cae54)))
print(hex(main(0x2be457ca)))


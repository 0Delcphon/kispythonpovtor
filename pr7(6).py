def main(x):
    A = x&0b111111111111111
    B = (x >> 15)&0b11111111111111
    C = (x >> 29)&0b11
    D = (x >> 31)&0b1

    fake = 0
    fake |= A
    fake |= B << 15
    fake |= D << 29
    fake |= C << 30

    return fake


print(hex(main(0xfc2fd4e6)))
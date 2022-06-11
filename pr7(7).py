def main(x):
    A = x&0b11111111111
    B = (x >> 11)&0b111111111
    C = (x >> 20)&0b111111111
    D = (x >> 29)&0b111

    fake = 0
    fake |= B
    fake |= A << 9
    fake |= C << 20
    fake |= D << 29

    return fake


print(hex(main(0x8ae8e100)))
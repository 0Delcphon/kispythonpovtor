def main(x):
    A = x&0b111111
    B = (x >> 6)&0b111
    C = (x >> 9)&0b1111
    D = (x >> 13)&0b111111
    E = (x >> 19)&0b11
    F = (x >> 21)&0b1111111111
    G = (x >> 31)&0b1

    fake = 0
    fake |= B
    fake |= A << 3
    fake |= C << 9
    fake |= F << 13
    fake |= E << 23
    fake |= D << 25
    fake |= G << 31
    return fake


print(hex(main(0xce0a4317)))
print(hex(main(0x07dbfb4b)))
print(hex(main(0xb6b81e69)))
print(hex(main(0x0c9c9bd1)))
print(hex(main(0xb003e68b)))
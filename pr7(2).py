def main(x):
    A = x&0b111
    B = (x >> 3)&0b1111111
    C = (x >> 10)&0b11111111111111
    D = (x >> 24)&0b111
    E = (x >> 27)&0b1
    F = (x >> 28)&0b111
    G = (x >> 31)&0b1

    fake = 0
    fake |= E
    fake |= C << 1
    fake |= F << 15
    fake |= G << 18
    fake |= D << 19
    fake |= B << 22
    fake |= A << 29
    return fake


print(hex(main(0xbd721c93)))
print(hex(main(0x8e39848d)))
print(hex(main(0xc59ee77c)))
print(hex(main(0xeb535663)))
print(hex(main(0xc5e4fdea)))
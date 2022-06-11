def main(x):
    A = x&0b1111111111
    B = (x >> 10)&0b111111111111
    C = (x >> 22)&0b1111
    D = (x >> 26)&0b1111
    E = (x >> 30)&0b1
    F = (x >> 31)&0b1

    fake = 0
    fake |= F
    fake |= C << 1
    fake |= D << 5
    fake |= E << 9
    fake |= B << 10
    fake |= A << 22

    return fake


print(hex(main(0x2ab722d3)))
print(hex(main(0x3dc68244)))
print(hex(main(0x33cba317)))
print(hex(main(0xf23a72fa)))
print(hex(main(0x530c4486)))
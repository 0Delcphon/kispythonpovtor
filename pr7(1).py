def main(x):
    A = x&0b111111111111
    B = (x>>12)&0b11
    C = (x>>14)&0b1111111111111111
    D = (x>>30)&0b1
    E = (x>>31)&0b1

    fake = 0
    fake|=C
    fake|=B << 16
    fake|=E << 18
    fake|=D << 19
    fake|=A << 20
    return fake


print(hex(main(0xa11a631a)))
print(hex(main(0x3bee9050)))
print(hex(main(0xd7beb165)))
print(hex(main(0xc40b72ad)))
print(hex(main(0x60482bb0)))
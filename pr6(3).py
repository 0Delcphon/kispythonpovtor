def main(x):
    if x[3] == 2018:
        if x[0] == 'PAWN':
            if x[2] == 1966:
                return 0
            if x[2] == 2008:
                return 1
            if x[2] == 1968:
                return 2
        if x[0] == 'MINID':
            return {1966: 3, 2008: 4, 1968: 5}[x[2]]
        if x[0] == 'LIMBO':
            return 6
    if x[3] == 1969:
        return 7
    if x[3] == 2012:
        if x[0] == 'PAWN':
            return 0
        if x[0] == 'MINID':
            return {1966: 9, 2008: 10, 1968: 11}[x[2]]
        if x[0] == 'LIMBO':
            return 12


print(main(['PAWN', 1995, 2008, 2018]))
print(main(['MINID', 2005, 1968, 2012]))
print(main(['LIMBO', 1995, 2008, 2012]))
print(main(['PAWN', 1995, 2008, 1969]))
print(main(['MINID', 2005, 1966, 2018]))
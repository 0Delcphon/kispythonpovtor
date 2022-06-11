def main(x):
    if x[1] == 2013:
        if x[3] == 1974:
            if x[2] == 'VOLT':
                return 0
            if x[2] == 'LFE':
                return 1
        if x[3] == 1986:
            return {'VOLT': 2, 'LFE': 3}[x[2]]
        if x[3] == 2014:
            return 4
    if x[1] == 1970:
        if x[3] == 1974:
            return 5
        if x[3] == 1986:
            return {1998: 6, 1988: 7, 2006: 8}[x[0]]
        if x[3] == 2014:
            return {1998: 9, 1988: 10, 2006: 11}[x[0]]


print(main([2006, 2013, 'LFE', 1974]))
print(main([1988, 1970, 'VOLT', 1974]))
print(main([1988, 1970, 'VOLT', 1986]))
print(main([2006, 1970, 'LFE', 2014]))
print(main([2006, 2013, 'LFE', 2014]))
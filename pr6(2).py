def main(x):
    if x[0] == 2014:
        if x[3] == 'PLSQL':
            if x[2] == 2010:
                if x[1] == 1964:
                    return 0
                if x[1] == 1965:
                    return 1
            if x[2] == 2008:
                return 2
        if x[3] == 'POD':
            return 3
    if x[0] == 2005:
        return 4
    if x[0] == 1967:
        if x[4] == 'ABNF':
            return 5
        if x[4] == 'UNO':
            if x[3] == 'PLSQL':
                return {1964: 6, 1965: 7}[x[1]]
            if x[3] == 'POD':
                return {2010: 8, 2008: 9}[x[2]]


print(main([2005, 1965, 2010, 'PLSQL', 'ABNF']))
print(main([1967, 1964, 2010, 'PLSQL', 'UNO']))
print(main([1967, 1964, 2010, 'POD', 'UNO']))
print(main([2014, 1965, 2008, 'PLSQL', 'UNO']))
print(main([1967, 1964, 2010, 'POD', 'ABNF']))
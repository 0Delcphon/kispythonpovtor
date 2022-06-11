def main(x):
    if x[4] == 1963:
        if x[2] == 'SCSS':
            if x[0] == 2015:
                return 0
            if x[0] == 1995:
                return 1
        if x[2] == 'PHP':
            return 2
        if x[2] == 'LOGOS':
            if x[0] == 2015:
                return {'CLICK': 3, 'HACK': 4, 'SAS': 5}[x[3]]
            if x[0] == 1995:
                return {'CLOCK': 6, 'HACK': 7, 'SAS': 8}[x[3]]
    if x[4] == 1974:
        return 9
    if x[4] == 1986:
        return 10


print(main([1995, 1994, 'PHP', 'HACK', 1974]))
print(main([1995, 1957, 'SCSS', 'SAS', 1963]))
print(main([2015, 1994, 'SCSS', 'CLICK', 1963]))
print(main([1995, 1957, 'PHP', 'SAS', 1963]))
print(main([1995, 1957, 'PHP', 'HACK', 1986]))
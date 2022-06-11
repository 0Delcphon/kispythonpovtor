def main(x):
    if x[2] == 2007:
        if x[0] == 1971:
            if x[3] == 'KRL':
                return 0
            if x[3] == 'VUE':
                return {'SVG': 1, 'IO': 2}[x[1]]
            if x[3] == 'DYLAN':
                return 3
        if x[0] == 1979:
            if x[3] == 'KRL':
                if x[1] == 'SVG':
                    return 4
                if x[1] == 'IO':
                    return 5
            if x[3] == 'VUE':
                return 6
            if x[3] == 'DYLAN':
                return 7
    if x[2] == 2000:
        return {1971: 8, 1979: 9}[x[0]]


print(main([1971, 'SVG', 2007, 'VUE', 2020]))
print(main([1979, 'IO', 2000, 'VUE', 1979]))
print(main([1971, 'SVG', 2000, 'KRL', 2005]))
print(main([1971, 'IO', 2007, 'DYLAN', 2020]))
print(main([1971, 'IO', 2007, 'KRL', 1979]))
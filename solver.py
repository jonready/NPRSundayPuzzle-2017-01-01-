def valid(names):
    arr = [tuple(n) for n in names]
    return arr == list(zip(*arr))

def cmp(*names):
    '''
    Transforms something like cmp(a, b, c, d, e)
    into e[0] == a[4] and e[1] == b[4] and e[2] == c[4] and e[3] == d[4]
    
    purely because the logic looks ugly and bothers me
    '''
    i = len(names)-1
    return names[-1][0:i] == ''.join([x[i] for x in names[:-1]])


def main():
    with open('filtered_names.csv', 'r') as f:
        names = f.read().upper().splitlines()
    '''
    desired = lambda r: len(r[1]) == 5 and r[3] == 'M' and \
                        int(r[2]) > 1890 and int(r[4]) > 20

    with open('NationalNames.csv', 'r') as f:
        names = sorted(list(set(r[1].upper() for r in filter(desired,
            (row.split(',') for row in f.read().splitlines())))))
    '''

    # print(len(names), 'names')

    buckets = [[] for _ in range(26)]
    hash = lambda c: ord(c)-65
    for n in names:
        buckets[hash(n[0])].append(n)

    for a in names:
        candidates = [[a]]
        for char in a[1:]:
            candidates.append(buckets[hash(char)])
        for b in candidates[1]:
            if cmp(a, b):
                for c in candidates[2]:
                    if cmp(a, b, c):
                        for d in candidates[3]:
                            if cmp(a, b, c, d): 
                                for e in candidates[4]:
                                    if cmp(a, b, c, d, e):
                                        if not valid([a, b, c, d, e]):
                                            exit('Algorithm is incorrect.')
                                        print(a, b, c, d, e)

if __name__ == '__main__':
    main()

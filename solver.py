import itertools

def valid(names):
    arr = [tuple(n) for n in names]
    return arr == list(zip(*arr))


def main():
    assert(valid(['ABRAM', 'BLANE', 'RANDY', 'ANDRE', 'MEYER']))
    assert(valid(['REECE', 'ERROL', 'ERNST', 'COSMO', 'ELTON']))
    assert(not valid(['ZZZZZ', 'ERROL', 'ERNST', 'COSMO', 'ELTON']))

    desired = lambda r: len(r[1]) == 5 and r[3] == 'M' and \
                        int(r[2]) > 1960 and int(r[4]) > 200

    with open('NationalNames.csv', 'r') as f:
        names = sorted(list(set(r[1].upper() for r in filter(desired,
            (row.split(',') for row in f.read().splitlines())))))

    # print(len(names), 'names')

    hash = lambda c: ord(c)-65
    buckets = [[] for _ in range(26)]
    for n in names:
        buckets[hash(n[0])].append(n)

    for n in names:
        candidates = [[n]]
        for c in n[1:]:
            candidates.append(buckets[hash(c)])
        for combo in itertools.product(*candidates):
            # print('trying', combo)
            if valid(combo):
                print(combo)


if __name__ == '__main__':
    main()

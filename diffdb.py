from typing import Iterable, Iterator, TypeVar
import sys

T = TypeVar('T')

def lines(it: Iterable[str], /) -> Iterator[str]:
    for part in it:
        for line in part.splitlines():
            if line:
                yield line

def pairs(it: Iterable[T], /) -> Iterator[tuple[T, T]]:
    it = iter(it)

    for left in it:
        try:
            right = next(it)
            yield left, right

        except StopIteration:
            pass

def readdb(filename: str) -> set[tuple[str, str]]:
    db = set[tuple[str, str]]()
    with open(filename, 'rt') as file:
        for i, pair in enumerate(pairs(lines(file))):
            try:
                [int(x) for s in pair for x in s.split()]
            except ValueError:
                raise ValueError(f'at lines ({i * 2, i * 2 + 1}): {pair}')
            db.add(pair)
    return db

dbl = readdb(sys.argv[1])
dbr = readdb(sys.argv[2])

strs = dbl.difference(dbr)

def strlen(s: str) -> int:
    return len([int(si) for si in s.split()])

def sorting(s: tuple[str, str]) -> tuple[int, int]:
    s1, s2 = s
    n1 = strlen(s1) + strlen(s2)
    n2 = len(s1) + len(s2)
    return n2, n1

for (l, r) in sorted(strs, key=sorting):
    n = min(strlen(l), strlen(r))
    print(l)
    # print(' '.join('0' for _ in range(n + 1)))
    print(r)
    # print(' '.join('0' for _ in range(n + 3)))

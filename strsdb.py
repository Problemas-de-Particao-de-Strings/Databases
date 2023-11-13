import pandas as pd
import sys

df = pd.read_csv(sys.argv[1])
df.dropna(inplace=True)

left = df['left'].str.strip('[]').str.split(',').str.join(' ')
right = df['right'].str.strip('[]').str.split(',').str.join(' ')

strs = set[tuple[str, str]]()
for (l, r) in zip(left, right):
    assert isinstance(l, str), l
    assert isinstance(r, str), r
    strs.add((l, r))

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

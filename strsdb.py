import pandas as pd


df = pd.read_csv('../Dados/FPT3-exact.csv')
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

for (l, r) in sorted(strs, key=lambda s: sum(strlen(si) for si in s)):
    n = min(strlen(l), strlen(r))
    print(l)
    # print(' '.join('0' for _ in range(n + 1)))
    print(r)
    # print(' '.join('0' for _ in range(n + 3)))

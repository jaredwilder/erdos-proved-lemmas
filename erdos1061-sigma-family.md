# Erdős #1061 — an infinite sigma solution family and a linear lower bound

Author: Jared Wilder. Public release: 2026-09-11.

Let `S(x)` count ordered pairs `(a,b)` with `a+b<=x` satisfying

`σ(a)+σ(b)=σ(a+b)`.

## Theorem 1 — infinite family

For every positive integer `a` with `gcd(a,6)=1`,

`σ(a)+σ(2a)=σ(3a)`.

### Proof

Multiplicativity gives

`σ(2a)=3σ(a)` and `σ(3a)=4σ(a)`,

so

`σ(a)+σ(2a)=σ(3a)`.

Each such `a` therefore yields the ordered solutions `(a,2a)` and `(2a,a)`.

## Theorem 2 — unconditional linear lower bound

Put `Y=floor(x/3)`. Then

`S(x) >= 2 * #{1<=a<=Y : gcd(a,6)=1}`.

Writing `Y=6q+r`, `0<=r<6`, the coprime count is

`2q + 1_{r>=1} + 1_{r>=5}`,

which is at least `Y/3-1/3`. Hence

`S(x) >= 2x/9 - 4/3`.

Therefore `S(x)=o(x)` is impossible. If `S(x)~cx` exists, then `c>=2/9`.

## Theorem 3 — neighboring diagonal is empty

For every positive integer `a`,

`2σ(a) != σ(2a)`.

Indeed, writing `a=2^k m` with `m` odd gives

`σ(2a)-2σ(a)=σ(m)>0`.

The proof is exact. Computational checks in the provenance archive independently reproduce both identities on finite ranges.

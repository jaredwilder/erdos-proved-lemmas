# Erdős #1061 — sigma solution families, linear lower bounds, and a killed counting bound

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

## Exact obstruction — the proposed `r(N) <= τ(N)` bound is false

For a fixed `N`, let

`r(N) = #{(a,b) : a+b=N and σ(a)+σ(b)=σ(N)}`

count ordered solutions on the `N`-diagonal, and let `τ(N)` be the divisor-counting function.

A historical route proposed the pointwise bound

`r(N) <= τ(N)`.

The release-day counterexample audit finally ran the exact finite computation that the route itself had requested. The bound is false. The first recovered failure is

`N=123`, where `r(123)=6 > τ(123)=4`.

The three unordered pairs are

- `(38,85)`, with `σ(38)+σ(85)=60+108=168=σ(123)`;
- `(41,82)`, with `42+126=168`;
- `(46,77)`, with `72+96=168`.

Further failures include

`r(141)=6 > 4`

and

`r(183)=8 > 4`.

By `N<=400`, the exact scan reaches `r(N)=10` for some diagonals. Thus any argument for #1061 that uses `r(N)<=τ(N)` as a load-bearing pointwise estimate is dead independently of the separate defect that originally caused that route to be retracted.

## Larger Erdős #1061 research program

This compact theorem entry is **not the full public #1061 surface**.

The provenance archive also contains `erdos1061-aliquot-square/`, which develops:

- an aliquot-square primitive-seed generator;
- a primitive-ray scaling theorem;
- an exact certificate bank of **152,803 primitive seeds** with `a+b<=200000`;
- an integer-only certificate verifier;
- a second exact generator search through `a<=5,000,000`;
- rigorous released linear-lower-bound coefficients above `2.29549` under the campaign's ordered-pair convention;
- a Mersenne-power specialization.

Together with the explicit failure of the naive divisor-count bound above, that material is now clearly problem-program scale. It should live in a dedicated Erdős #1061 repository once a writable shell exists; this theorem-bank file remains the concise entry point until then.

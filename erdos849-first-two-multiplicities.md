# Erdős #849 — exact `t=1` and `t=2` binomial-representation slices

Author: Jared Wilder. Public release: 2026-09-11.

For an integer `a`, count solutions of

`C(n,k)=a`

under the canonical restriction

`1<=k<=n/2`.

## Theorem

- `a=3` has exactly one admissible solution.
- `a=10` has exactly two admissible solutions.

Thus the multiplicities `t=1` and `t=2` both occur.

## Proof for `a=3`

The solution with `k=1` is

`C(3,1)=3`.

If `k>=2`, then `n>=2k>=4`, and therefore

`C(n,k)>=C(4,2)=6>3`.

So `(n,k)=(3,1)` is the unique admissible solution.

## Proof for `a=10`

There are two solutions:

`C(10,1)=10`,

and

`C(5,2)=10`.

If `k>=3`, then `n>=2k>=6`, so

`C(n,k)>=C(6,3)=20>10`.

For `k=2`, the equation `n(n-1)/2=10` has the unique positive solution `n=5`.

Hence exactly two admissible solutions exist.

## Scope

This proves only the first two multiplicities. The general question asks which larger multiplicities occur and remains separate.

Historical novelty is not claimed.
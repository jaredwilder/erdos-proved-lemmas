# Erdős #849 — exact binomial-representation multiplicities `t=1,2,3,4`

Author: Jared Wilder. Public release: 2026-09-11.

For an integer `a`, count solutions of

`C(n,k)=a`

under the canonical restriction

`1<=k<=n/2`.

## Theorem

The first four positive multiplicities all occur exactly:

- `a=3` has exactly 1 solution;
- `a=10` has exactly 2 solutions;
- `a=120` has exactly 3 solutions;
- `a=3003` has exactly 4 solutions.

The complete admissible solution sets are

`3: (3,1)`

`10: (5,2), (10,1)`

`120: (10,3), (16,2), (120,1)`

`3003: (14,6), (15,5), (78,2), (3003,1)`.

## Exact finite verification principle

For `k=1`, the only possible solution is `n=a`.

For `k>=2` and `k<=n/2`, one has

`C(n,k)>=C(n,2)=n(n-1)/2`.

Therefore any solution with `k>=2` satisfies

`n(n-1)/2<=a`,

so only finitely many `n` need checking. Direct exact evaluation of the binomial coefficients in this finite range gives precisely the solution lists above.

For the first two values there are also immediate hand proofs:

- if `a=3`, every `k>=2` gives at least `C(4,2)=6`;
- if `a=10`, the `k=2` equation gives `n=5`, while every `k>=3` gives at least `C(6,3)=20`.

The `t=3,4` witnesses are classical and are recorded on the maintained Erdős Problems page; historical novelty is not claimed.

## Scope

This proves the multiplicities `1,2,3,4`. The general problem asks whether every `t` occurs; no examples are currently known for `t>=5` in the maintained public record.
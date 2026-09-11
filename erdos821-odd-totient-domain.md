# Erdős #821 — odd totient targets above 1 have no preimages

Author: Jared Wilder. Public release: 2026-09-11.

Let

`g(n)=#{m>=1 : phi(m)=n}`.

## Theorem

For every odd integer `n>1`,

`g(n)=0`.

## Proof

For every `m>=3`, the reduced residue classes modulo `m` pair under `a -> -a`. No unit is fixed by this pairing: `a≡-a (mod m)` would imply `2a≡0`, and since `a` is a unit this would force `m|2`.

Therefore `phi(m)` is even for every `m>=3`. The only odd totient value is `phi(1)=phi(2)=1`.

Thus no odd target greater than 1 lies in the image of Euler's totient function.

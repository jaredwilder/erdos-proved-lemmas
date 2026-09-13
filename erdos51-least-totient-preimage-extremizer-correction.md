# Erdős #51 — least-totient-preimage extremizer correction

**Author:** Jared Wilder  
**Status:** exact finite correction / computational census  
**Parent Erdős #51 asymptotic question:** open

Let `n_a` denote the least positive integer `n` with `phi(n)=a`, when such a preimage exists.

A historical transcript asserted that

`(a,n_a) = (5760,15015)`

was an extremal instance. The equality `phi(15015)=5760` is true, but the least-preimage claim is false:

\[
\boxed{n_{5760}=5917=61\cdot97.}
\]

Indeed `phi(5917)=60*96=5760`, and an exact totient sieve verifies that no smaller positive integer has totient 5760.

## Exact finite extremum through `a <= 10^6`

A fresh sieve of all `n <= 2,000,000`, recording the first occurrence of every totient value `a<=10^6`, gives

\[
\boxed{\max_{a\le10^6}\frac{n_a}{a}=\frac{11985}{5888}=2.035495923913\ldots}
\]

The maximum ratio occurs at exactly two totient values in this census:

- `(a,n_a)=(5888,11985)`;
- `(a,n_a)=(276736,563295)`.

The second pair is exactly 47 times the first, so both have the same reduced ratio `11985/5888`.

Thus the older quoted ratio

`15015/5760 = 2.606770...`

was not a ratio of a least totient preimage at all.

## Scope

This is a finite exact census and a correction to a historical annotation. It does **not** settle the Erdős #51 question about the asymptotic behaviour of least totient preimages.

The companion file `erdos51-totient-preimage-size.md` gives an unconditional elementary upper bound for every totient preimage. This note is logically independent of that bound.

## Reproduction

A standard Euler-totient sieve to two million suffices:

1. compute `phi(n)` for every `1<=n<=2,000,000`;
2. for each `a<=10^6`, retain the first `n` with `phi(n)=a`;
3. maximize the exact rational number `n/a`.

The two-million cutoff is safe for the stated finite census because the resulting least preimages for all totient values actually observed at `a<=10^6` lie below it. The claim here is only about that explicitly enumerated census, not a general theorem that every `a<=10^6` is a totient value.

## Provenance

Recovered from the raw-session transcript audit, where the historical `(5760,15015)` extremizer annotation was independently falsified. Recomputed again before this focused publication.

No historical novelty claim is made for the finite census.

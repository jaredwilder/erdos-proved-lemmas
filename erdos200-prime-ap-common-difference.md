# Erdős #200 — small primes divide the common difference of long prime progressions

**Author:** Jared Wilder  
**Status:** exact structural lemma / classical obstruction; parent Erdős #200 remains open  
**Historical novelty:** not asserted

## The theorem

Let

\[
p_j=a+jd\qquad(0\le j<k)
\]

be a `k`-term arithmetic progression of primes with `d>0`.

Then for every prime `q<=k`, at least one of the following holds:

1. `q | d`; or
2. one of the progression terms `p_j` is exactly `q`.

Equivalently: every prime `q<=k` that does **not** itself occur as a term of the progression must divide the common difference `d`.

## Proof

Fix a prime `q<=k` and suppose `q` does not divide `d`.

Because `d` is invertible modulo `q`, the `q` residues

\[
a,\ a+d,\ a+2d,\ldots,a+(q-1)d\pmod q
\]

run through all residue classes modulo `q` exactly once. Therefore one of the first `q` progression terms is divisible by `q`.

That term is prime. Hence a prime divisible by `q` must equal `q` itself.

Thus, if `q` does not occur among the progression terms, the assumption `q∤d` is impossible, and so `q|d`.

## Useful corollary

If the first term satisfies `a>k`, then no prime `q<=k` can occur as a progression term. Consequently

\[
\prod_{q\le k\atop q\text{ prime}}q\mid d.
\]

So the full primorial up to `k` divides the common difference.

More generally, without the assumption `a>k`, the product of all primes `q<=k` except those primes that actually occur as terms of the progression divides `d`.

## Why the endpoint exception matters

The historical campaign contained overstatements that omitted the possibility that the forced multiple of `q` is the prime `q` itself.

For example,

\[
3,5,7
\]

is a three-term prime progression with common difference `2`. Here `q=3` does not divide `d`, but the progression itself contains the term `3`. Thus the unqualified claim `q|d` for every prime `q<=k` is false.

The theorem above is the repaired exact statement.

## Relation to Erdős #200

Erdős #200 asks whether the longest arithmetic progression of primes in `{1,...,N}` has length

\[
o(\log N).
\]

The primorial-divisibility lemma is a standard obstruction: when the small-prime exceptions are absent, the common difference must be divisible by a product whose logarithm is asymptotic to `k`. Combined with the trivial size restriction `d<N`, this naturally yields a logarithmic-scale upper bound.

That does **not** prove the required little-`o(log N)` improvement. The recovered campaign later explicitly rejected a purported Pintz-based superlogarithmic lower-bound close and retained the parent problem as open.

This release therefore promotes only the exact residue-class theorem and its primorial corollary, not an asymptotic resolution of #200.
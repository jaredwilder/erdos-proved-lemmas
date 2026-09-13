# Erdős #260 — correction: the binary-indicator reduction drops the coefficient `a_n`

**Author:** Jared Wilder  
**Status:** route correction / exact refutation of a recovered campaign reduction  
**Parent problem:** remains open in this record

The frozen Erdős #260 campaign asks about strictly increasing integer sequences `(a_n)` with

\[
\frac{a_n}{n}\to\infty
\]

and the arithmetic nature of

\[
\boxed{\sum_{n\ge1}\frac{a_n}{2^{a_n}}}.
\]

A later Pass-3 route claimed an affirmative close by identifying the series with the binary indicator of the set

\[
A=\{a_1,a_2,\ldots\},
\]

namely with

\[
\sum_{k\in A}2^{-k},
\]

and then invoking the standard fact that rational binary expansions are eventually periodic.

That reduction is false: it drops the coefficient `a_n`.

## Smallest exact refutation

For the one-term set `A={2}`,

\[
\sum \frac{a_n}{2^{a_n}}=\frac{2}{2^2}=\frac12,
\]

whereas the purported binary-indicator quantity is

\[
\sum_{k\in A}2^{-k}=2^{-2}=\frac14.
\]

Thus the two expressions are not identical even in the smallest nontrivial example.

More generally,

\[
\sum_n\frac{a_n}{2^{a_n}}
=\sum_{k\ge1} k\,\mathbf 1_A(k)\,2^{-k},
\]

not

\[
\sum_{k\ge1}\mathbf 1_A(k)\,2^{-k}.
\]

The factors `k` create carries in base 2, so the rationality question cannot be reduced to eventual periodicity of the bare membership indicator without a new argument controlling those carries.

## What survives

A separate elementary statement in the same route is correct:

> If an infinite set `A={a_1<a_2<...}` is eventually periodic with some positive period `p`, then `a_n/n` is bounded.

Indeed, an infinite eventually periodic set is eventually a nonempty union of residue classes modulo `p`, so its gaps are bounded by `p`; hence `a_n <= C+pn` and `a_n/n` is bounded.

But this correct observation does **not** establish irrationality of

\[
\sum a_n2^{-a_n},
\]

because the missing step is precisely the invalid coefficient-dropping identification above.

## Authority / provenance

The recovered campaign contains both:

- the frozen statement with the coefficient `a_n` in the numerator; and
- later `R006` rows that describe `sum 2^{-a_n}` as the "exact carry-free reduction."

The two are not the same mathematical object. This file records the semantic mismatch explicitly so that local `PROVED` / `COMPUTATION_SUPPORTED` labels attached to the indicator-series route cannot be mistaken for a close of Erdős #260.

No conclusion about the truth or falsehood of the original Erdős #260 statement is made here.

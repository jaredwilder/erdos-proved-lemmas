# Erdős #289 — all-prime p-adic obstruction for integral reciprocal sums

**Author:** Jared Wilder  
**Public release:** 2026-09-14

## Theorem

Let `S` be a finite set of integers at least `2`, and suppose

\[
\sum_{n\in S}\frac1n\in\mathbb Z.
\]

Fix any prime `p`, and define

\[
A_p=\left\{\frac np:n\in S,\ p\mid n\right\}.
\]

Then

\[
\boxed{
v_p\!\left(\sum_{m\in A_p}\frac1m\right)\ge1.
}
\]

In words: after extracting one factor of `p` from every denominator divisible by `p`, the resulting reciprocal subfamily sum must itself be divisible by `p` in the `p`-adic sense.

## Proof

Split

\[
S=S_0\sqcup S_1,
\]

where

\[
S_0=\{n\in S:p\nmid n\},\qquad
S_1=\{n\in S:p\mid n\}.
\]

Let

\[
I=\sum_{n\in S}\frac1n\in\mathbb Z.
\]

Every denominator in the `S_0` sum is a `p`-adic unit, so

\[
\sum_{n\in S_0}\frac1n
\]

has nonnegative `p`-adic valuation. The integer `I` also has nonnegative `p`-adic valuation. Hence

\[
\sum_{n\in S_1}\frac1n
=I-\sum_{n\in S_0}\frac1n
\]

is `p`-adically integral.

But by definition of `A_p`,

\[
\sum_{n\in S_1}\frac1n
=\frac1p\sum_{m\in A_p}\frac1m.
\]

Therefore

\[
v_p\!\left(\frac1p\sum_{m\in A_p}\frac1m\right)\ge0,
\]

which is equivalent to

\[
v_p\!\left(\sum_{m\in A_p}\frac1m\right)\ge1.
\]

## Relation to the classical 2-adic obstruction

The case `p=2` contains the familiar parity mechanism behind Kürschák-type nonintegrality arguments for reciprocal sums over consecutive intervals. The theorem here is the corresponding statement simultaneously for every prime.

## Scope

This is a structural necessary condition. It does not by itself solve Erdős #289 or classify all integral reciprocal decompositions.

The historical estate source records exact finite sanity checks in addition to this proof, but the universal theorem above is analytic and does not rely on those computations. Priority of the all-prime formulation is not asserted.
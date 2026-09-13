# Erdős #829 — a divisor bound for sums of two positive cubes

**Author:** Jared Wilder  
**Status:** proved child theorem + correction of a stale false close  
**Parent problem:** the polylogarithmic representation bound remains open in the recovered estate

Let

\[
r(n)=\#\{(a,b)\in\mathbb N^2:a^3+b^3=n\},
\]

with ordered pairs counted, matching the additive convolution convention for the indicator of the positive cubes.

## Theorem

For every positive integer `n`,

\[
\boxed{r(n)\le 2\tau(n).}
\]

Here `τ(n)` is the number of positive divisors of `n`.

## Proof

Suppose

\[
a^3+b^3=n.
\]

Set

\[
d=a+b.
\]

Using

\[
a^3+b^3=(a+b)(a^2-ab+b^2),
\]

we have `d|n`. Once `d` is fixed, put `q=n/d`. Then

\[
q=a^2-ab+b^2=(a+b)^2-3ab=d^2-3ab,
\]

so

\[
ab=\frac{d^2-q}{3}
   =\frac{d^2-n/d}{3}.
\]

Thus for each divisor `d|n`, both the sum `a+b=d` and product `ab` are determined. The two numbers `a,b` are roots of

\[
t^2-dt+ab=0.
\]

Therefore each divisor `d` contributes at most one unordered pair `{a,b}`, hence at most two ordered pairs `(a,b)` and `(b,a)`.

Summing over the `τ(n)` possible positive divisors `d` gives

\[
r(n)\le2\tau(n).
\]

No computation or asymptotic input is needed.

## Why this does not settle Erdős #829

The canonical question asks whether

\[
r(n)\ll (\log n)^{O(1)}
\]

uniformly in `n`.

The divisor function has super-polylogarithmic maximal order, so the bound `r(n)≤2τ(n)` is too weak by itself to imply the desired polylogarithmic estimate.

It is still a useful exact structural reduction: every cube representation is controlled by a divisor `a+b` together with a quadratic reconstruction.

## Correction: the stale “Mahler closes branch B” row is false

One historical campaign row claimed that a construction of Mahler gives

\[
r(n)>(\log n)^K
\]

infinitely often for **every** fixed `K`, which would literally refute the canonical polylogarithmic conjecture.

The later estate audit explicitly retracts that strength. The cited Mahler-type constructions yield lower bounds by a **fixed** power of `log n` (with later improvements also at fixed powers); they do not produce growth beyond every fixed power of `log n`. The campaign itself later records that no super-polylogarithmic witness is known and that both close branches remain open.

Accordingly:

- `r(n)≤2τ(n)`: **proved**;
- “Mahler gives `r(n)>(log n)^K` for every fixed `K`”: **rejected strength inflation**;
- canonical polylogarithmic upper bound: **not closed here**.

## Convention note

Several early finite-enumeration records accidentally compared unordered representation counts to the ordered additive convolution. For example, ordered convolution doubles non-diagonal pairs. This note fixes the convention at the outset and the theorem is stated for ordered pairs.

## Provenance / novelty boundary

Recovered from route R004 of the Erdős #829 campaign and re-adjudicated against the later external audit during the 2026-09-13 release court. Historical novelty is not asserted for the divisor reduction.
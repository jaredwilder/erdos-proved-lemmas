# Erdős #930 — infinite Pell family of square-product interval pairs

**Author:** Jared Wilder  
**Status:** exact infinite-family theorem + threshold obstruction for `r=2`; parent existence question for large interval length remains open  
**Historical novelty:** not asserted

## Parent setting

Erdős #930 asks whether, for every fixed number `r` of pairwise disjoint intervals of consecutive positive integers, there exists a length threshold `k` such that whenever all `r` intervals have length at least `k`, the product of every integer in all intervals is **not** a perfect power.

This note treats the slice `r=2`.

## Theorem 1 — infinitely many length-2 square-product pairs

Let `(x,y)` be a positive integer solution of the Pell equation

\[
x^2-24y^2=1
\]

with `x>5`, and put

\[
a=\frac{x-1}{2}.
\]

Then the two intervals

\[
I_1=\{2,3\},
\qquad
I_2=\{a,a+1\}
\]

are disjoint and satisfy

\[
\prod_{m\in I_1\cup I_2}m=(6y)^2.
\]

Consequently there are infinitely many disjoint pairs of length-2 intervals whose total product is a perfect square.

### Proof

Every solution of `x^2-24y^2=1` has odd `x`, so `a=(x-1)/2` is integral. Moreover

\[
a(a+1)
=\frac{(x-1)(x+1)}4
=\frac{x^2-1}{4}
=6y^2.
\]

Therefore

\[
\prod_{m\in I_1\cup I_2}m
=2\cdot3\cdot a(a+1)
=6\cdot6y^2
=(6y)^2.
\]

The fundamental positive Pell solution is `(x,y)=(5,1)`, which gives `a=2` and hence overlapping intervals. Every later positive solution has `x>5`, so `a>=24` and the two intervals are disjoint.

There are infinitely many positive solutions, generated for example by

\[
x_t+y_t\sqrt{24}=(5+\sqrt{24})^t,
\qquad t=1,2,3,\ldots.
\]

Discarding `t=1` leaves infinitely many disjoint interval pairs.

The first such example is

\[
\{2,3\},\{24,25\},
\]

whose product is

\[
2\cdot3\cdot24\cdot25=3600=60^2.
\]

## Theorem 2 — any `r=2` threshold must satisfy `k>=4`

No threshold `k<=3` can work in the `r=2` parent problem.

### Proof

The Pell family above gives disjoint intervals of length `2` with perfect-square total product, so thresholds `k=1` and `k=2` fail.

For length `3`, take

\[
I_1=\{1,2,3\},
\qquad
I_2=\{48,49,50\}.
\]

Then

\[
\prod_{m\in I_1\cup I_2}m
=1\cdot2\cdot3\cdot48\cdot49\cdot50
=705600
=840^2.
\]

Thus `k=3` also fails. Hence any valid threshold for `r=2` must obey

\[
\boxed{k\ge4}.
\]

## Boundary

The theorem does **not** show that no threshold exists for `r=2`. The recovered campaign found no length-raising mechanism: scaling preserves square-product structure but does not turn a length-`k` interval into a length-`k+1` interval. The regime `k>=4` remained unresolved.

So the surviving result is exactly:

- an infinite Pell family at length `2`;
- an exact length-`3` square witness;
- the rigorous lower bound `k(2)>=4` for any putative threshold.

No novelty claim is made.
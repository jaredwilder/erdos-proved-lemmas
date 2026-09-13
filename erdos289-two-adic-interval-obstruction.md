# Erdős #289 — unique maximal 2-adic denominator obstruction

**Author:** Jared Wilder  
**Status:** exact structural theorem / obstruction; parent construction problem not closed  
**Historical novelty:** not asserted; Kürschák-type 2-adic argument

## Theorem 1 — one interval can never sum to an integer

Let

\[
I=\{a,a+1,\ldots,b\},\qquad 1\le a<b.
\]

Then

\[
\sum_{n=a}^{b}\frac1n\notin\mathbb Z.
\]

In particular, no nontrivial consecutive reciprocal interval has sum `1`.

## Lemma — unique maximal `v_2`

Among the integers in any finite consecutive interval containing at least two integers, there is a unique element with maximal 2-adic valuation.

### Proof

Suppose two distinct integers `x<y` in the interval both had the same maximal valuation `e=v_2(x)=v_2(y)`.

Write

\[
x=2^e u,\qquad y=2^e v
\]

with `u,v` odd. Then `v-u` is a positive even integer, so between `u` and `v` there is an even integer `w`. Consequently

\[
2^e w
\]

lies strictly between `x` and `y` and has 2-adic valuation at least `e+1`, contradicting maximality.

Thus the maximum occurs uniquely.

## Proof of Theorem 1

Let

\[
L=\operatorname{lcm}(a,a+1,\ldots,b).
\]

Write

\[
\sum_{n=a}^{b}\frac1n=\frac1L\sum_{n=a}^{b}\frac{L}{n}.
\]

Let `m` be the unique denominator in the interval with maximal `v_2(m)`. Since the interval contains at least one even integer, this maximal valuation is at least `1`, and

\[
v_2(L)=v_2(m).
\]

Therefore `L/m` is odd. For every other `n`,

\[
v_2(n)<v_2(L),
\]

so `L/n` is even.

Hence the cleared numerator

\[
\sum_{n=a}^{b}L/n
\]

is odd. Since `L` is even, the fraction cannot be an integer.

## Theorem 2 — parity constraint for several interval blocks

Consider finitely many nontrivial consecutive intervals `I_1,...,I_r`, allowing repetitions, and suppose

\[
\sum_{j=1}^r\sum_{n\in I_j}\frac1n
\]

is an integer.

Let `E` be the largest 2-adic valuation attained by any denominator appearing in any block. Then the number of blocks whose internal maximal denominator valuation equals `E` must be even.

### Proof

Clear a common lcm `L` of all denominators. A contribution is odd after clearing precisely when its denominator has valuation `E`.

By the lemma, each block attaining level `E` contributes exactly one such odd term; every other contribution is even. Because `E>=1`, integrality forces the total cleared numerator to be even. Hence the number of odd contributions—and therefore the number of blocks attaining the global maximal level—must be even.

## Boundary for Erdős #289

The recovered campaign explored representations of `1` by sums of reciprocal interval blocks. The 2-adic theorem above is a genuine necessary obstruction, but it does not by itself construct representations for all large block counts or rule them out for infinitely many counts.

Later campaign state explicitly recognized that the parity condition is satisfiable and is not a parent close. This release therefore promotes the exact p-adic obstruction only.

No novelty claim is made.
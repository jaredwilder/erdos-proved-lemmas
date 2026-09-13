# Erdős #289 — all-prime p-adic obstruction and the 2-adic interval ledger

**Author:** Jared Wilder  
**Status:** exact structural theorem / obstruction; parent construction problem not closed  
**Historical novelty:** not asserted; the `p=2` interval mechanism is Kürschák-type

## Theorem 0 — an obstruction at every prime

Let `S` be a finite set of integers `>=2` and suppose

\[
T:=\sum_{n\in S}\frac1n\in\mathbb Z.
\]

Fix any prime `p`, and define

\[
A_p=\{n/p:n\in S,\ p\mid n\}.
\]

Then

\[
\boxed{
v_p\!\left(\sum_{m\in A_p}\frac1m\right)\ge1.
}
\]

In words: after stripping exactly one factor of `p` from every denominator in `S` divisible by `p`, the reciprocal sum of that stripped subfamily must itself be divisible by `p` in the p-adic sense.

### Proof

Split the integer reciprocal sum into denominators prime to `p` and denominators divisible by `p`:

\[
T
=
\sum_{\substack{n\in S\\p\nmid n}}\frac1n
+
\sum_{\substack{n\in S\\p\mid n}}\frac1n.
\]

Put

\[
U=\sum_{\substack{n\in S\\p\nmid n}}\frac1n,
\qquad
V=\sum_{m\in A_p}\frac1m.
\]

Then

\[
T=U+\frac1pV.
\]

Every denominator occurring in `U` is prime to `p`, so `U` is p-adically integral:

\[
v_p(U)\ge0.
\]

Also `T` is an ordinary integer, hence `v_p(T)>=0`. Therefore

\[
\frac1pV=T-U
\]

is p-adically integral. Thus

\[
v_p(V)-1\ge0,
\]

which is exactly

\[
v_p(V)\ge1.
\]

This proves the all-prime obstruction.

### Interpretation

An integer reciprocal sum cannot be certified prime-by-prime merely by total denominator clearing. For **every** prime occurring in the denominators, the p-divisible subfamily must satisfy its own induced divisibility condition after one p-factor is removed.

The `p=2` case is the source of the parity mechanisms below.

---

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

---

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

Equivalently, in p-adic language the top 2-adic level cannot occur with odd multiplicity in an integral sum.

---

## Authority boundary

The recovered estate records the all-prime theorem as a source-level `PROVED` statement and reports finite exact sanity checks, but it is **not kernel-certified** at universal scope. The proof above is therefore supplied explicitly and stands independently of the historical workflow label.

The recovered #289 campaign explores representations of `1` by sums of reciprocal interval blocks. These p-adic conditions are genuine necessary obstructions, but they do not by themselves construct representations for all large block counts or rule them out for infinitely many counts.

Later campaign state explicitly recognized that the 2-adic parity condition is satisfiable and is not a parent close. This release promotes the all-prime obstruction and its exact 2-adic interval consequences only.

No novelty claim is made.
# Erdős #291 — corrected leading-base-`p` harmonic criterion

**Author:** Jared Wilder  
**Status:** exact structural theorem / registry-corruption repair  
**Historical novelty:** not asserted

## Setup

Let

\[
L_n=\operatorname{lcm}(1,2,\ldots,n),
\qquad
A_n=\sum_{k=1}^{n}\frac{L_n}{k}.
\]

Thus

\[
H_n=\sum_{k=1}^{n}\frac1k=\frac{A_n}{L_n}.
\]

Fix a prime `p<=n`. Let `p^e` be the largest power of `p` not exceeding `n`, and put

\[
q=\left\lfloor\frac{n}{p^e}\right\rfloor.
\]

Because `p^(e+1)>n`, one has `1<=q<p`.

## The theorem

Let `u_q/v_q` be `H_q` in lowest terms. Then

\[
\boxed{
 p\mid\gcd(A_n,L_n)
 \iff
 p\mid u_q.
}
\]

Equivalently, the relevant harmonic test is at the **leading base-`p` digit**

\[
q=\left\lfloor n/p^e\right\rfloor,
\]

not at `floor(n/p)`.

## Proof

Since `p<=n`, the `p`-adic valuation of `L_n` is exactly `e`:

\[
v_p(L_n)=e.
\]

Reduce `A_n` modulo `p`.

If `v_p(k)<e`, then

\[
\frac{L_n}{k}\equiv0\pmod p.
\]

So only those `k` with `v_p(k)=e` can contribute modulo `p`.

Because `p^e` is the largest power of `p` at most `n`, those integers are exactly

\[
k=p^e j,
\qquad 1\le j\le q.
\]

Moreover `q<p`, so none of `1,...,q` is divisible by `p`. Therefore in `F_p`,

\[
A_n
\equiv
\sum_{j=1}^{q}\frac{L_n}{p^e j}
=
\frac{L_n}{p^e}\sum_{j=1}^{q}j^{-1}
\pmod p.
\]

The factor `L_n/p^e` is a unit modulo `p`. Hence

\[
p\mid A_n
\iff
\sum_{j=1}^{q}j^{-1}\equiv0\pmod p.
\]

The sum on the right is `H_q` modulo `p`. Since every denominator `1,...,q` is prime to `p`, the reduced denominator `v_q` is also prime to `p`. Thus

\[
H_q\equiv0\pmod p
\iff
p\mid u_q.
\]

Finally `p|L_n` automatically, so `p|A_n` is equivalent to `p|gcd(A_n,L_n)`. This proves the theorem.

## Why the older `floor(n/p)` criterion is false

A recovered historical registry row used `H_{floor(n/p)}`. That is the wrong scale once `p^2<=n`.

For example take

\[
n=20,\qquad p=3.
\]

The largest power of `3` not exceeding `20` is `9`, so the corrected index is

\[
q=\lfloor20/9\rfloor=2.
\]

Now

\[
H_2=\frac32,
\]

whose numerator is divisible by `3`.

But the stale index gives `floor(20/3)=6`, and

\[
H_6=\frac{49}{20},
\]

whose numerator is not divisible by `3`.

Thus the `floor(n/p)` formulation is genuinely false and must not be resurrected from old `PROVED` rows.

## Boundary

This criterion controls one prime at a time in the divisibility of the unreduced harmonic numerator `A_n`. It does not by itself settle the parent #291 infinitude/density questions.

The release promotes the corrected universal theorem and records the supersession explicitly.
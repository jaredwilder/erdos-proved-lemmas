# Erdős #243 — eventual-divisibility irrationality barrier

**Author:** Jared Wilder  
**Status:** exact child theorem / structural obstruction; parent Erdős #243 converse remains open in this estate  
**Historical novelty:** not asserted; this is a re-derived Kürschák-type argument

## The theorem

Let

\[
a_1<a_2<a_3<\cdots
\]

be positive integers. Assume that there is an index `n0` such that

\[
a_n\mid a_{n+1}\qquad(n\ge n_0)
\]

and

\[
\frac{a_{n+1}}{a_n}\longrightarrow\infty.
\]

Then

\[
\sum_{n=1}^{\infty}\frac1{a_n}\notin\mathbb Q.
\]

The finite prefix before `n0` is irrelevant, so the theorem also covers chains whose divisibility begins only eventually.

## Proof

Because the ratio tends to infinity, the reciprocal series converges. Suppose for contradiction that

\[
S=\sum_{n=1}^{\infty}\frac1{a_n}\in\mathbb Q.
\]

Subtract the finite rational prefix through `n0-1`. Thus

\[
T:=\sum_{n=n_0}^{\infty}\frac1{a_n}=\frac pq
\]

for some integers `p` and `q>0`.

Choose a real number `R>q+1`. Since `a_{n+1}/a_n -> infinity`, choose `M>=n0` so that

\[
\frac{a_{n+1}}{a_n}\ge R
\]

for every `n>=M`.

By eventual divisibility,

\[
a_k\mid a_M\qquad(n_0\le k\le M).
\]

Hence

\[
q a_M\sum_{k=n_0}^{M}\frac1{a_k}\in\mathbb Z.
\]

Also

\[
q a_M T=p a_M\in\mathbb Z.
\]

Their difference is therefore an integer:

\[
q a_M\sum_{k=M+1}^{\infty}\frac1{a_k}\in\mathbb Z.
\]

But the tail is strictly positive, while repeated use of `a_{n+1}>=R a_n` gives

\[
0<q a_M\sum_{k=M+1}^{\infty}\frac1{a_k}
\le q\sum_{j=1}^{\infty}R^{-j}
=\frac{q}{R-1}
<1.
\]

No integer lies strictly between `0` and `1`, a contradiction. Therefore `S` is irrational.

## Consequence for Erdős #243

The frozen #243 campaign studies increasing integer sequences satisfying

\[
\frac{a_n}{a_{n-1}^2}\to1
\]

and asks whether rationality of `sum 1/a_n` forces the eventual Sylvester-type recurrence

\[
a_n=a_{n-1}^2-a_{n-1}+1.
\]

The theorem above does **not** prove that converse. What it does prove is a useful structural exclusion:

> Any rational-sum counterexample to the #243 conclusion must fail `a_n | a_{n+1}` infinitely often.

In particular, no eventually divisible chain with ratios tending to infinity can supply a counterexample.

## Estate audit boundary

The recovered campaign recorded this result as a standing `PROVED` Kürschák-type lemma. Later falsifier and obligation passes continued to treat it as surviving mathematics while refusing the leap from this restricted obstruction to the full #243 parent statement.

This release independently reconstructs the proof above rather than relying on the historical status bit.

The parent problem remains open in this estate. No novelty claim is made for the classical-style irrationality argument.
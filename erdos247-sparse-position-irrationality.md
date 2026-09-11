# Erdős #247 — eventual-periodicity barrier in every integer base

**Author:** Jared Wilder  
**Recovered:** September 2026 MSL audit / Pass-3 synthesis  
**Public promotion:** 2026-09-11

Let `b>=2` be an integer and `A⊂N`. Define

\[
x_A=\sum_{a\in A}b^{-a}.
\]

## Theorem 1 — exact rationality characterization

\[
\boxed{
x_A\in\mathbb Q
\iff
1_A(n)\text{ is eventually periodic}.
}
\]

### Proof

The displayed series is a base-`b` expansion whose digits are exactly the `0/1` indicator sequence of `A`; no carries occur because `1<b`.

If the indicator is eventually periodic, split the expansion into a finite prefix plus finitely many geometric progressions. The value is rational.

Conversely, a rational real has an eventually periodic base-`b` expansion. The only representation ambiguity relevant to a `0/1` digit string occurs in base 2 at terminating dyadic rationals, where the alternative expansion has an eventually-all-1 tail. That alternative is itself eventually periodic. Hence the `0/1` support sequence is eventually periodic whenever `x_A` is rational.

## Corollary 2 — unbounded gaps force irrationality

If `A={a_1<a_2<...}` is infinite and

\[
\sup_n(a_{n+1}-a_n)=\infty,
\]

then

\[
\boxed{\sum_n b^{-a_n}\notin\mathbb Q.}
\]

Indeed an infinite eventually periodic `0/1` sequence containing infinitely many 1s has bounded gaps between successive 1s.

## Corollary 3 — the Erdős-hypothesis slice

If

\[
\limsup_{n\to\infty}\frac{a_n}{n}=\infty,
\]

then the gaps are unbounded: bounded gaps would imply `a_n=O(n)`. Hence

\[
\boxed{\sum_{n\ge1}b^{-a_n}\text{ is irrational}.}
\]

The original base-2 theorem is one instance of this all-base result.

## Companion density equivalence

If

\[
A(N)=\#\{n:a_n\le N\},
\]

then

\[
\boxed{
\limsup a_n/n=\infty
\iff
\liminf A(N)/N=0.
}
\]

One direction evaluates at `N=a_n`, where `A(a_n)=n`. Conversely, along `N_j` with `A(N_j)/N_j→0`, set `n_j=A(N_j)+1`; then `a_{n_j}>N_j` and `a_{n_j}/n_j→∞`.

## Scope and literature

Erdős #247 asks for **transcendence** under the sparsity hypothesis; everything here is an irrationality theorem / characterization only.

The eventual-periodicity characterization is likely textbook/folklore territory. The September audit found no exact match for the problem-specific hypothesis in targeted searches, but specialist literature review was incomplete. No historical priority claim is made for the general base-expansion fact.

Original subject extraction: `jaredwilder/unpublished-math-papers/erdos247-sparse-binary-irrationality/`.

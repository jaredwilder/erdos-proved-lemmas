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

## Theorem 4 — density/sparsity equivalence

If

\[
A(N)=\#\{n:a_n\le N\},
\]

then

\[
\boxed{
\limsup_{n\to\infty} a_n/n=\infty
\iff
\liminf_{N\to\infty} A(N)/N=0.
}
\]

### Proof

If `a_{n_j}/n_j -> infinity`, take `N_j=a_{n_j}`. Then `A(N_j)=n_j`, so

\[
A(N_j)/N_j=n_j/a_{n_j}\to0.
\]

Conversely, choose `N_j` with `A(N_j)/N_j->0` and put `n_j=A(N_j)+1`. Then `a_{n_j}>N_j`, hence

\[
\frac{a_{n_j}}{n_j}>
\frac{N_j}{A(N_j)+1}\to\infty.
\]

## Correction history — a valid route was killed by an impossible counterexample

The release-day counterexample audit recovered a historical route (`R013`) that had been marked killed because it supposedly contradicted Theorem 4. The proposed counterexample required simultaneously

`limsup a_n/n = infinity`

and

`liminf A(N)/N = 1`.

That combination is impossible. Since always `A(N)<=N`, the second condition forces `A(N)/N->1`; evaluating at `N=a_n` gives `n/a_n->1`, hence `a_n/n->1`, contradicting the first condition.

Thus the historical kill was invalid. The density equivalence above is restored as an elementary exact theorem and should not be treated as a retired route.

## Scope and literature

Erdős #247 asks for **transcendence** under the sparsity hypothesis; everything here is an irrationality theorem / characterization only.

The eventual-periodicity characterization is likely textbook/folklore territory. The September audit found no exact match for the problem-specific hypothesis in targeted searches, but specialist literature review was incomplete. No historical priority claim is made for the general base-expansion fact.

Original subject extraction: `jaredwilder/unpublished-math-papers/erdos247-sparse-binary-irrationality/`.

# Erdős #1104 — monotonicity of the triangle-free chromatic extremum

**Author:** Jared Wilder  
**Release:** 2026-09-11

Let `f(n)` be the maximum chromatic number of a triangle-free graph on `n` vertices. Then

\[
\boxed{f(n+1)\ge f(n).}
\]

## Proof

Take an `n`-vertex triangle-free graph `G` with chromatic number `f(n)`. Append one isolated vertex. The resulting `(n+1)`-vertex graph remains triangle-free and has the same chromatic number as `G`. Therefore

\[
f(n+1)\ge\chi(G)=f(n).
\]

## Scope boundary

This is exact monotonicity bookkeeping. It does not establish the asymptotic growth sought in the parent problem and carries no novelty claim.

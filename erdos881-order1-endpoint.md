# Erdős #881 — exact order-1 endpoint construction

**Author:** Jared Wilder  
**Release:** 2026-09-11

For the `k=1` endpoint of the frozen #881 formulation, take

\[
A=\mathbb N,
\qquad
B=\{n:n\equiv2\pmod4\}.
\]

Then `A` is a minimal asymptotic basis of order 1, while `A\B` is an asymptotic basis of order 2.

## Verification

`A=N` is trivially an asymptotic basis of order 1. It is minimal: deleting any `m` permanently removes `m` itself from the one-term representation set.

Now

\[
A\setminus B=\{n:n\not\equiv2\pmod4\}.
\]

Every sufficiently large integer is a sum of two members of this set. Residue-by-residue modulo 4 one may choose summands with allowed residue pairs

\[
0=0+0,
\quad1=0+1,
\quad2=1+1,
\quad3=0+3
\pmod4,
\]

and take the summands positive and large enough. Thus the complement of `B` inside `A` is an asymptotic basis of order 2.

## Scope boundary

This settles only the order-1 endpoint construction. It does not settle the higher-order parent problem. The recovered estate notes that a broader 2026 public claim already covers this stratum, so no novelty claim is made here.

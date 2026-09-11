# Erdős #535 — exact normalization of a common pairwise gcd

**Author:** Jared Wilder  
**Public routing:** 2026-09-11  
**Source:** Pass-3 promoted reduction, independently rechecked

Let `a_1,...,a_r` be positive integers with `r>=2`, and let `d` be a positive integer.

## Theorem

The following are equivalent:

1. for every distinct `i,j`,
   \[
   \gcd(a_i,a_j)=d;
   \]
2. `d` divides every `a_i`, and after writing
   \[
   b_i=a_i/d,
   \]
   the integers `b_1,...,b_r` are pairwise coprime.

Equivalently,

\[
\boxed{
\gcd(a_i,a_j)=d\ \forall i\ne j
\iff
\gcd(a_i/d,a_j/d)=1\ \forall i\ne j.
}
\]

## Proof

If every pair has gcd `d`, then `d` divides every member (take any partner), and

\[
\gcd(a_i/d,a_j/d)=\frac{\gcd(a_i,a_j)}d=1.
\]

Conversely, if `a_i=db_i` and the `b_i` are pairwise coprime, then

\[
\gcd(a_i,a_j)=d\gcd(b_i,b_j)=d.
\]

## Scope

This is an exact structural reduction. It turns the equal-pairwise-gcd condition into the pairwise-coprime case after factoring out the common gcd. It does not by itself settle the extremal parent problem.

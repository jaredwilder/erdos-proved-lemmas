# Erdős #938 — three consecutive squares are never a 3-term arithmetic progression

**Author:** Jared Wilder  
**Public routing:** 2026-09-11  
**Source:** Pass-3 non-PROVED route candidate; universal identity independently rechecked

## Theorem

For every integer `n`, the three squares

\[
n^2,\quad(n+1)^2,\quad(n+2)^2
\]

do not form a three-term arithmetic progression.

Equivalently,

\[
\boxed{2(n+1)^2-n^2-(n+2)^2=-2.}
\]

## Proof

Expand:

\[
2(n^2+2n+1)-n^2-(n^2+4n+4)=-2.
\]

A three-term arithmetic progression would require the left side to be zero, which never occurs.

## Scope

This removes the most immediate square subfamily from the search for arithmetic progressions among consecutive powerful numbers. It does not settle the corresponding problem for general powerful numbers.

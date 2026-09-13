# Erdős #126 — no three distinct positive integers have all pairwise sums powers of two

**Author:** Jared Wilder  
**Status:** exact universal structural obstruction; standalone local lemma  
**Historical novelty:** not asserted

## Theorem

There do not exist three distinct positive integers

\[
0<x<y<z
\]

such that all three pairwise sums

\[
x+y,\qquad x+z,\qquad y+z
\]

are powers of `2`.

## Proof

Suppose for contradiction that

\[
x+y=2^p,\qquad x+z=2^q,\qquad y+z=2^r.
\]

Since `x<y<z`,

\[
x+y<x+z<y+z,
\]

so

\[
p<q<r.
\]

Adding the first two equations and subtracting the third gives

\[
2x=2^p+2^q-2^r.
\]

But `p<q`, so

\[
2^p+2^q<2^{q+1}.
\]

And `r>q` implies

\[
2^r\ge2^{q+1}.
\]

Therefore

\[
2^p+2^q-2^r<0,
\]

which would force `x<0`, contradicting positivity.

Hence no such triple exists.

## Boundary

The recovered estate records this as a small universal obstruction arising inside the broader Erdős #126 program. It is not presented as a resolution of the parent problem, and no novelty claim is made for the elementary argument.
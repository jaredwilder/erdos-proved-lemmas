# Erdős #341 — the seed `{1}` generates exactly the odd integers

**Author:** Jared Wilder  
**Status:** exact seed-classification theorem; parent arbitrary-seed periodicity question remains open  
**Historical novelty:** not asserted

## Greedy rule

Start from the finite seed `A={1}`. Having chosen

\[
a_1<a_2<\cdots<a_n,
\]

let `a_{n+1}` be the least integer greater than `a_n` that is **not** representable as

\[
a_i+a_j
\]

with `1<=i,j<=n`; the two summands may coincide.

## The theorem

For every `n>=1`,

\[
\boxed{a_n=2n-1.}
\]

Hence the greedy sequence is

\[
1,3,5,7,9,\ldots
\]

and its gap sequence is identically `2`, so it is periodic with period `1`.

## Proof

We argue by induction.

The first term is `a_1=1`. Since

\[
2=1+1,
\]

`2` is forbidden, while `3` is not a sum of two chosen terms. Thus `a_2=3`.

Assume the chosen terms are exactly

\[
1,3,5,\ldots,2n-1.
\]

The next integer after the current maximum is `2n`, and

\[
2n=1+(2n-1),
\]

so it is forbidden.

But every chosen term is odd, so every pairwise sum of chosen terms is even. Therefore the next integer

\[
2n+1
\]

is not representable as such a sum. By greediness it is the next selected term:

\[
a_{n+1}=2n+1.
\]

This completes the induction.

## Boundary

The frozen #341 campaign asks about eventual periodicity of the gap sequence for much more general finite initial seeds. This theorem settles only the exact seed `A={1}`.

The recovered campaign explicitly kept the arbitrary-seed problem open while marking this seed computation as a hand-proved exact theorem. No novelty claim is made for this elementary slice.
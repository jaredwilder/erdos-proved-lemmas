# Erdős #359 — universal quadratic upper bound for the true greedy sequence

**Author:** Jared Wilder  
**Status:** exact universal child theorem for the `n=1` greedy sequence; parent asymptotic questions remain open  
**Historical novelty:** not asserted

## Exact greedy rule

Start with

\[
a_1=1.
\]

Given `a_1<...<a_k`, let `S_k` be the set of sums of all nonempty **consecutive index blocks**:

\[
S_k=\left\{a_i+a_{i+1}+\cdots+a_j:1\le i\le j\le k\right\}.
\]

Then define `a_{k+1}` to be the least integer strictly larger than `a_k` that does not belong to `S_k`.

Singleton blocks are included.

## Theorem

For every `k>=1`,

\[
\boxed{
a_{k+1}\le \frac{k(k+1)}2+1.
}
\]

In particular `a_k=O(k^2)`.

## Key invariant

For every `k>=1`,

\[
\boxed{\{1,2,\ldots,a_k\}\subseteq S_k.}
\]

### Proof

At `k=1`, `a_1=1` and `S_1={1}`.

Assume the invariant holds at stage `k`. By definition, `a_{k+1}` is the least integer greater than `a_k` missing from `S_k`. Therefore every integer

\[
a_k+1,a_k+2,\ldots,a_{k+1}-1
\]

belongs to `S_k`.

When `a_{k+1}` is adjoined, it is itself a singleton consecutive block, so `a_{k+1}\in S_{k+1}`. Also `S_k\subseteq S_{k+1}`. Hence

\[
\{1,2,\ldots,a_{k+1}\}\subseteq S_{k+1}.
\]

The invariant follows by induction.

## Proof of the quadratic bound

At stage `k`, the number of nonempty consecutive index intervals `[i,j]` is exactly

\[
1+2+\cdots+k=\frac{k(k+1)}2.
\]

Different intervals may have the same sum, so

\[
|S_k|\le\frac{k(k+1)}2.
\]

By the greedy definition and the invariant,

\[
\{1,2,\ldots,a_{k+1}-1\}\subseteq S_k.
\]

Therefore

\[
a_{k+1}-1\le |S_k|\le\frac{k(k+1)}2,
\]

which gives

\[
a_{k+1}\le\frac{k(k+1)}2+1.
\]

## Sanity check on the exact sequence

The initial terms under the frozen consecutive-block semantics begin

\[
1,2,4,5,8,10,\ldots
\]

For example, from `1,2,4,5,8`, the consecutive block sums contain `9=4+5` but do not contain `10`, so the next term is `10`.

This matters because a historical green receipt in the estate encoded an incorrect early prefix. The proof above does not depend on that receipt or on any finite prefix computation.

## Boundary

Erdős #359 asks substantially stronger density and asymptotic questions, including whether for the `n=1` sequence `a_k/k -> infinity` and whether `a_k/k^(1+c) -> 0` for every `c>0`.

The quadratic bound proves only an `O(k^2)` upper estimate. It does not settle those sharper limits or the general-start density problem.

No novelty claim is made.
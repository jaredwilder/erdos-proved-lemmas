# Erdős #373 — a prime obstruction and three exact factorial-product witnesses

**Author:** Jared Wilder  
**Status:** elementary theorem + exact witnesses  
**Parent finiteness problem:** open in this record

Consider solutions of

\[
n! = a_1!a_2!\cdots a_k!
\]

with

\[
n-1>a_1\ge a_2\ge\cdots\ge a_k\ge2.
\]

The recovered #373 campaign contains a clean prime obstruction and several exact solutions. This note promotes only the mathematics that is directly checkable without relying on the campaign's conflicting early finite-census rows.

## Prime obstruction

If `n>=3` and `n-1` is prime, then no such solution exists.

### Proof

Put

\[
p=n-1.
\]

Because `a_1<n-1`, every factor satisfies

\[
a_i\le n-2=p-1<p.
\]

Hence the prime `p` divides none of the factorials `a_i!`, so

\[
p\nmid a_1!\cdots a_k!.
\]

But `p=n-1<=n`, so

\[
p\mid n!.
\]

This contradicts the proposed factorial-product identity. Therefore no solution exists whenever `n-1` is prime. ∎

## Three exact solutions

The same recovered campaign records the following solutions.

### `n=9`

\[
\boxed{9!=7!\,3!\,3!\,2!}.
\]

Indeed,

\[
\frac{9!}{7!}=8\cdot9=72
\]

and

\[
3!\,3!\,2!=6\cdot6\cdot2=72.
\]

The required strict top inequality holds:

\[
8>7\ge3\ge3\ge2.
\]

### `n=10`

\[
\boxed{10!=7!\,6!}.
\]

Indeed,

\[
\frac{10!}{7!}=8\cdot9\cdot10=720=6!.
\]

Again

\[
9>7\ge6.
\]

### `n=16`

\[
\boxed{16!=14!\,5!\,2!}.
\]

Indeed,

\[
\frac{16!}{14!}=15\cdot16=240
\]

while

\[
5!\,2!=120\cdot2=240.
\]

And

\[
15>14\ge5\ge2.
\]

## What is deliberately not claimed

One later campaign verifier reports that, for `2<=n<=36`, these are exactly the solutions. An earlier row in the same historical campaign incorrectly claimed no solution through `n=9`, contradicting the explicit `n=9` witness above. Because the historical finite-census layer contains that stale conflict, this note does **not** promote the `n<=36` classification without a fresh independent replay.

Likewise, none of the facts above decides whether only finitely many `n` admit such factorizations.

## Provenance

Recovered independently in the Pass-3 and Pass-6 #373 dossiers. The prime obstruction survived the campaign's falsification pass as a one-line divisibility theorem, and the three displayed identities are verified here directly from factorial arithmetic.

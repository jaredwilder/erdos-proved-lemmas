# Erdős #727 — an infinite prime obstruction family

**Author:** Jared Wilder  
**Status:** exact strong partial; parent problem remains open  
**Novelty:** not asserted here

## Parent question

Fix `k≥2`. Are there infinitely many integers `n` such that

\[
(n+k)!^2\mid(2n)!\ ?
\]

The estate does **not** settle that existence question. It does contain an exact infinite family on which divisibility always fails.

## Theorem

Fix an integer

\[
k\ge2.
\]

For every prime

\[
p>2k,
\]

set

\[
n=p-k.
\]

Then

\[
\boxed{(n+k)!^2\nmid(2n)!}.
\]

Consequently, for every fixed `k≥2`, there are infinitely many non-witnesses.

## Proof

Since `n+k=p`,

\[
(n+k)!^2=(p!)^2.
\]

Therefore

\[
v_p((n+k)!^2)=2.
\]

On the other hand,

\[
2n=2p-2k.
\]

The hypothesis `p>2k` gives

\[
p<2p-2k<2p.
\]

Hence among the positive integers up to `2n=2p-2k`, exactly one is divisible by `p`, namely `p` itself. Thus

\[
v_p((2n)!)=1.
\]

So

\[
v_p((2n)!)
<
v_p((n+k)!^2),
\]

which proves

\[
(n+k)!^2\nmid(2n)!.
\]

There are infinitely many primes `p>2k`, so this gives infinitely many non-witnesses for every fixed `k`.

## Scope

This is an obstruction family, not a negative solution of the parent problem. A fixed `k` could still have infinitely many other values of `n` for which the required divisibility holds.

The result is useful because any successful construction must avoid an explicit infinite prime-indexed family lying at

\[
n=p-k.
\]

The recovered campaign explicitly retained this valuation argument as a true child theorem even though later routes did not close the existence question.

# Erdős #1073 — factorial-plus-one roughness and the square-root witness barrier

**Author:** Jared Wilder  
**Status:** proved structural child theorem + rejection of a stale false close  
**Parent problem:** the `A(x) ≤ x^{o(1)}` question remains open here

Let `A(x)` count composite integers `u<x` for which

\[
u\mid n!+1
\]

for at least one positive integer `n`.

## Theorem 1 — every prime factor exceeds the factorial index

If

\[
u\mid n!+1
\]

and `p` is any prime divisor of `u`, then

\[
\boxed{p>n.}
\]

### Proof

If `p≤n`, then `p|n!`. Since `p|u` and `u|n!+1`, we would also have `p|n!+1`. Subtracting gives `p|1`, impossible.

Thus every prime factor of `u` is strictly greater than `n`.

## Corollary 2 — composite witnesses lie above `n²`

If `u` is composite and `u|n!+1`, then

\[
\boxed{u>n^2.}
\]

Indeed, a composite positive integer has at least two prime factors counted with multiplicity. Every such factor is `>n`, so their product is `>n²`.

Equivalently,

\[
\boxed{n<\sqrt u.}
\]

Therefore every `u<x` counted by `A(x)` admits its factorial witness in the restricted range

\[
 n<\sqrt x.
\]

This is an exact reduction of the witness-index range, not an asymptotic solution of the counting problem.

## Example

The bound is nonvacuous: `u=25` is composite and

\[
4!+1=25,
\]

so `u=25` is counted for every `x>25`. Its least prime factor `5` indeed exceeds the witness index `4`.

## Rejected historical close — Wilson does not extend this way to prime powers

A stale campaign row claimed that odd prime powers automatically provide many counted `u`, using a purported Wilson-type statement for prime powers, and from this asserted a lower bound of order `π(sqrt x)` that would refute the canonical `x^{o(1)}` conjecture.

That step is false.

For the smallest instructive example,

\[
8!+1=40321\equiv1\pmod9,
\]

not `0 mod 9`.

The generalized Wilson theorem about the product of units modulo certain prime powers is **not** the statement that `(p^a-1)! ≡ -1 (mod p^a)`. The factorial contains nonunits and the substitution is invalid.

The estate's later external audit independently records this exact `mod 9` refutation and quarantines the claimed branch-B close.

## Scope

What is proved here is:

- all prime factors of every factorial-plus-one divisor exceed the factorial index;
- every composite counted witness satisfies `u>n²`;
- consequently any `u<x` can be witnessed only by `n<sqrt(x)`.

What is **not** proved here is the canonical subpolynomial estimate

\[
A(x)\le x^{o(1)}.
\]

Turning the square-root witness window into a subpolynomial count requires substantial additional control on how many relevant divisors `n!+1` can contribute below `x`. No such transfer is asserted in this note.

Historical novelty is not claimed; the point is to preserve the exact surviving structural theorem while permanently separating it from the false prime-power Wilson route.
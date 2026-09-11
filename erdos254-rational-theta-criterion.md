# Erdős #254 — exact rational-`theta` divergence criterion

**Author:** Jared Wilder  
**Public routing:** 2026-09-11

Let

\[
\theta=\frac aq\in(0,1)
\]

be reduced, and let `A⊆N`.

## Theorem

\[
\boxed{
\sum_{n\in A}\|\theta n\|=\infty
\iff
A\text{ contains infinitely many }n\text{ with }q\nmid n.
}
\]

Here `||x||` denotes distance to the nearest integer.

## Proof

If `q|n`, then `theta n` is an integer, so `||theta n||=0`.

If `q∤n`, coprimality of `a,q` implies `an mod q` is nonzero. Therefore the fractional part of `an/q` is one of

\[
\frac1q,\frac2q,\ldots,\frac{q-1}{q},
\]

and hence

\[
\left\|\frac{an}{q}\right\|\ge\frac1q.
\]

Thus infinitely many nonmultiples of `q` contribute at least `1/q` each, forcing divergence. Conversely, if only finitely many elements of `A` are nonmultiples of `q`, all but finitely many summands vanish, so the sum is finite.

## Scope

This exactly characterizes the rational-`theta` hypothesis in the #254 investigation. It does not establish the parent subset-sum conclusion and makes no historical novelty claim.
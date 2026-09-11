# Erdős #968 — exact prime-ratio monotonicity equivalence

**Author:** Jared Wilder  
**Release:** 2026-09-11

Let

\[
u_n=\frac{p_n}{n},
\qquad
d_n=p_{n+1}-p_n.
\]

Then

\[
\boxed{
u_n<u_{n+1}
\iff n d_n>p_n
\iff d_n>\frac{p_n}{n}.}
\]

## Proof

Starting from

\[
\frac{p_n}{n}<\frac{p_{n+1}}{n+1},
\]

cross-multiply by the positive denominator `n(n+1)`:

\[
(n+1)p_n<n p_{n+1}.
\]

Subtract `np_n` from both sides:

\[
p_n<n(p_{n+1}-p_n)=nd_n.
\]

Dividing by `n>0` gives the final equivalent form.

## Scope boundary

This is an exact algebraic reduction. It converts the target set into a prime-gap threshold condition but does not establish the positive lower density demanded by the parent problem.

The estate separately records that large-gap results imply infinitude of indices satisfying the inequality; that is explicitly weaker than the density target and is not promoted here as a close.

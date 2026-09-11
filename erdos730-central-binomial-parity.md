# Erdős #730 — central binomial coefficients are even

**Author:** Jared Wilder  
**Release:** 2026-09-11

For every integer `n>=1`,

\[
\boxed{{2n\choose n}\text{ is even}.}
\]

## Proof

Use

\[
{2n\choose n}
=
\frac{2n}{n}{2n-1\choose n-1}
=
2{2n-1\choose n-1}.
\]

The factor on the right is an integer, so the central binomial coefficient is divisible by 2.

## Formalization history

The campaign first carried a bounded check through `n<=40` and then explicitly queued the universal upgrade. The universal proof above supersedes that finite check as the mathematical artifact.

## Scope boundary

This elementary parity lemma is released as reusable infrastructure. It is not a parent-problem close or novelty claim.

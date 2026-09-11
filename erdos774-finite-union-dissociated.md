# Erdős #774 — finite union implies proportionately dissociated

**Author:** Jared Wilder  
**Release:** 2026-09-11

Suppose

\[
A=A_1\cup\cdots\cup A_k
\]

and each `A_i` is dissociated. Then every finite `B⊂A` contains a dissociated subset of cardinality at least

\[
\boxed{|B|/k}.
\]

## Proof

The sets `B∩A_i` cover `B`. Hence by the pigeonhole principle some index `i` satisfies

\[
|B\cap A_i|\ge |B|/k.
\]

Because dissociativity is hereditary, `B∩A_i` is dissociated. Taking this intersection gives the required subset.

## Scope boundary

This is the easy finite-union direction. The parent problem asks for substantially more, including converse-type structure. No novelty claim is attached to this elementary lemma.

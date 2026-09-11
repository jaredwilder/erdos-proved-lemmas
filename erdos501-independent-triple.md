# Erdős #501 — repaired finite independent-triple lemma

**Author:** Jared Wilder  
**Public routing:** 2026-09-11

Let `V` be an `N`-element set. Suppose each vertex has a directed forbidden row containing at most `m` vertices. Call an unordered pair bad when at least one orientation is forbidden.

## Theorem

If

\[
\boxed{6m<N-1,}
\]

then there exist three vertices containing no bad pair.

## Proof

There are at most `mN` directed forbidden incidences, so there are at most `mN` bad unordered pairs. Every bad pair belongs to at most `N-2` unordered triples. Therefore the number of triples contaminated by at least one bad pair is at most

\[
mN(N-2).
\]

If `6m<N-1`, then

\[
mN(N-2)<\frac{N(N-1)(N-2)}6={N\choose3}.
\]

Hence not every triple is contaminated, and an independent triple exists.

## Repair record

The historical proof used an unjustified factor-of-two improvement in the bad-pair count. The safe bound `#bad pairs<=mN` already proves the displayed threshold.

## Scope

This is a finite theorem only. The continuum parent problem needs an additional transfer theorem that is not supplied here.

The original extraction remains archived in `unpublished-math-papers/erdos501-independent-triple/`.

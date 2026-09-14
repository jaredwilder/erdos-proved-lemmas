# Erdős #1212 — an infinite isolated family in the admissible coprime-lattice graph

**Author:** Jared Wilder  
**Public release:** 2026-09-14

## Target graph

Work in the lattice graph on pairs `(x,y) in N^2` with `gcd(x,y)=1`, where unit coordinate moves are edges. The Erdős #1212 admissible-vertex predicate further requires

- `min(x,y)>1`, and
- at least one coordinate is composite.

The parent problem asks for an infinite injective admissible path whose coordinate sum tends to infinity.

## Theorem

For every integer `k>=2`,

\[
\boxed{(2,3^k)}
\]

is an isolated vertex of the admissible subgraph.

More precisely, in the full coprime lattice graph `(2,3^k)` has exactly one neighbor:

\[
\boxed{(1,3^k)}.
\]

Thus the family gives infinitely many explicit admissible dead ends.

## Proof

For `k>=2`, `3^k` is composite and

\[
\gcd(2,3^k)=1,
\]

so `(2,3^k)` is admissible.

Its four possible unit-coordinate moves are

\[
(1,3^k),\quad (3,3^k),\quad (2,3^k-1),\quad (2,3^k+1).
\]

Now:

- `gcd(1,3^k)=1`, so `(1,3^k)` is a neighbor in the ambient coprime graph;
- `gcd(3,3^k)=3`, so `(3,3^k)` is not a vertex of that graph;
- `3^k` is odd, hence both `3^k-1` and `3^k+1` are even, so
  \[
  \gcd(2,3^k\pm1)=2,
  \]
  and neither `(2,3^k-1)` nor `(2,3^k+1)` is a coprime-lattice vertex.

Therefore `(1,3^k)` is the unique ambient neighbor. But it fails the admissibility condition `min(x,y)>1`. Hence `(2,3^k)` has no admissible neighbor at all.

## Scope

This is an infinite structural obstruction family, not a resolution of Erdős #1212. The parent question remains whether some other admissible component contains an infinite path tending to infinity.

The campaign also contains local run bounds and finite dead-end examples, but they are not needed for this theorem. Targeted estate prior-art searches found no exact collision for this family; no historical novelty claim is made here.
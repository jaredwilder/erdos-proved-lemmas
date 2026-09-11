# Erdős #1085 — exact one-dimensional unit-distance extremum

Author: Jared Wilder. Public release: 2026-09-11.

## Theorem

For `n>=1`, the maximum number `f_1(n)` of unit-distance pairs determined by `n` distinct points on the real line is

`f_1(n)=n-1`.

## Proof

Let `X` be a finite set of `n` distinct real numbers. Form the graph whose vertices are the points of `X`, with an edge whenever two points are distance `1` apart.

Every connected component of this graph is a finite path: after choosing the leftmost point of a component, all other vertices in that component lie successively at offsets `1,2,...`, and a point can have at most one unit-distance neighbor to its left and at most one to its right. In particular the graph is a forest.

A forest on `n` vertices has at most `n-1` edges, so there are at most `n-1` unit-distance pairs.

Equality is attained by the arithmetic progression

`0,1,...,n-1`,

which has exactly the `n-1` consecutive unit-distance pairs.

Hence `f_1(n)=n-1`.

## Scope

This is the exact one-dimensional slice. Higher-dimensional unit-distance extremal problems are separate.

Historical novelty is not claimed.
# Erdős #1212 — exact row-run coordinate for the coprime lattice graph

**Author:** Jared Wilder  
**Status:** exact parent-specific structural coordinate; parent infinite-path problem remains open  
**Historical novelty:** not asserted

## Graph setting

Consider the graph whose vertices are pairs

\[
(x,y)\in\mathbb N^2
\]

with

\[
\gcd(x,y)=1,
\]

and where two vertices are adjacent when they differ by `±1` in exactly one coordinate.

The parent Erdős #1212 problem imposes additional path constraints (`min(x,y)>1` and at least one coordinate composite). This note isolates only the exact fixed-row geometry used by the campaign.

## A deliberately defined dual run function

For an integer `m>=2`, define

\[
g_*(m)
=
\min\Bigl\{L\ge1:\text{ every block of }L\text{ consecutive integers contains an integer not coprime to }m\Bigr\}.
\]

This notation is introduced here on purpose. It is **not** being identified with a standard Jacobsthal convention.

Equivalently, `g_*(m)-1` is the longest possible run of consecutive integers all coprime to `m`.

For example,

\[
g_*(3)=3,
\qquad
g_*(5)=5.
\]

Indeed the longest runs avoiding multiples of `3` and `5` have lengths `2` and `4`, respectively.

## Theorem 1 — exact fixed-row run length

Let

\[
\operatorname{rad}(x)=\prod_{p\mid x}p
\]

be the squarefree radical. For every `x>=2`, the maximum number of consecutive integers

\[
y,y+1,\ldots,y+L-1
\]

for which all lattice points

\[
(x,y),(x,y+1),\ldots,(x,y+L-1)
\]

are vertices of the coprime graph is exactly

\[
\boxed{g_*(\operatorname{rad}(x))-1.}
\]

### Proof

For every integer `y`,

\[
\gcd(x,y)=1
\iff
\gcd(\operatorname{rad}(x),y)=1.
\]

So a vertical run of graph vertices on row `x` is exactly a run of consecutive integers all coprime to `rad(x)`.

By definition of `g_*`, no run of `g_*(rad(x))` consecutive integers can be entirely coprime to `rad(x)`, while minimality of `g_*` guarantees the existence of a run of length `g_*(rad(x))-1` containing no non-coprime integer.

Hence the maximum run length is exactly

\[
g_*(\operatorname{rad}(x))-1.
\]

## Exact examples

### Row `x=9`

Here `rad(9)=3` and `g_*(3)=3`, so the maximum vertical run length is `2`.

For instance

\[
(9,25),(9,26)
\]

are consecutive vertices, while `27` is blocked by the factor `3`.

### Row `x=25`

Here `rad(25)=5` and `g_*(5)=5`, so the maximum run length is `4`.

The block

\[
y=6,7,8,9
\]

is a tight example; `5` and `10` are blocked by the factor `5`.

## Theorem 2 — even rows have no vertical edge

If `x` is even, no two vertically adjacent points on row `x` can both be vertices of the coprime graph.

### Proof

If `gcd(x,y)=1` and `x` is even, then `y` must be odd. Both neighbors `y-1` and `y+1` are even, so

\[
\gcd(x,y\pm1)\ge2.
\]

Thus neither vertical neighbor is a graph vertex.

So every even row has vertical degree zero.

## Semantic correction preserved

Historical campaign records used several incompatible descriptions of a function denoted `g`. One stale boundary-audit line described it as a maximum difference between consecutive coprime integers, which would give the wrong value at `m=3`. The later certifier explicitly defines the quantity by the **least block length forcing a non-coprime integer**, yielding `g_*(3)=3` and `g_*(5)=5`.

This release therefore avoids the ambiguous historical symbol and defines `g_*` explicitly.

## Boundary for Erdős #1212

The parent asks for an infinite path satisfying additional composite-coordinate and `min>1` constraints. The fixed-row theorem shows that an infinite admissible path cannot simply climb forever on one row; even rows cannot support a vertical move at all, and every odd fixed row has a finite coprime-run deadline.

That does **not** settle whether a multi-row infinite path exists. The recovered campaign correctly identified the remaining issue as a global row-transition / CRT-type construction problem.

No novelty claim is made for the elementary row-coordinate identity.
# Erdős #197 — every finite set admits a 3-AP-avoiding order

**Author:** Jared Wilder  
**Status:** proved finite child theorem  
**Parent problem:** the infinite partition/bijection problem remains open in this estate

## The theorem

Let `S` be any finite subset of the positive integers. Then there exists a linear ordering of `S` containing no increasing three-term arithmetic progression in positional order.

Equivalently, one can order `S` so that there are no values

\[
x<y<z,\qquad x+z=2y,
\]

that appear in the order as

\[
x\prec y\prec z.
\]

A stronger equivalent “beautiful-order” formulation is convenient: there are no positions `i<j<k` whose values satisfy

\[
2a_j=a_i+a_k.
\]

## Construction

Proceed recursively on the largest binary scale / on the size of the finite set.

Split

\[
S=S_{\mathrm{odd}}\sqcup S_{\mathrm{even}}.
\]

Order the odd elements first, using recursively an avoiding order after the affine map

\[
x\mapsto \frac{x-1}{2},
\]

and then order the even elements, using recursively an avoiding order after

\[
x\mapsto \frac{x}{2}.
\]

Because `S` is finite, repeated division by two eventually reaches singleton/empty sets, so the recursion terminates.

## Proof

Suppose for contradiction that positions `i<j<k` in the constructed order satisfy

\[
2a_j=a_i+a_k.
\]

If `a_i` and `a_k` have opposite parity, their sum is odd, impossible because the left-hand side is even.

So the two endpoints have the same parity.

If the midpoint `a_j` has the opposite parity from the endpoints, then it lies in the other top-level parity block. Since the construction places the entire odd block before the entire even block, it cannot lie positionally between two elements of the same parity block. Contradiction.

Therefore all three values have the same parity. Dividing all three by `2` in the even case, or applying `(x-1)/2` in the odd case, preserves the arithmetic-progression equation and preserves their relative order inside the recursively ordered block. This produces a forbidden triple one recursion level lower.

Repeated descent is impossible because the finite construction terminates. Hence no forbidden triple exists.

## Example

For `S=[8]`, the recursion gives the familiar order

```text
1, 5, 3, 7, 2, 6, 4, 8.
```

The recovered campaign independently checked this witness against all three-term arithmetic progressions in `[8]` with exact integer arithmetic.

## Consequence for finite colourings

For every `N` and every two-colouring / partition

\[
[N]=A\sqcup B,
\]

each finite part separately admits such an avoiding order. Thus **no finite initial-segment search can distinguish the two branches of Erdős #197**: every finite partition looks compatible with the affirmative direction after its two parts are separately reordered.

This is a structural finite theorem, not merely a computation.

## Why this does not solve Erdős #197

The canonical problem asks whether

\[
\mathbb N=A\sqcup B
\]

can be partitioned so that **both infinite parts admit genuine bijective enumerations** avoiding monotone three-term arithmetic progressions.

The finite parity recursion does not automatically define such an enumeration of an infinite set. For example, an “all odds first, then evens” order on an infinite set can exhaust infinitely many odd elements before ever reaching the even block; it is not automatically an order of type `ω`, hence not automatically a bijection `\mathbb N\simeq S`.

Likewise, the existence of avoiding orders on every finite truncation does not by itself supply a compatible inverse-limit order whose two colour classes are both enumerated bijectively by `\mathbb N`.

That finite-to-infinite compactness/order-type step is the load-bearing missing object in the recovered campaign. So:

- **all finite sets:** proved;
- **all finite two-partitions:** both parts separately avoidable;
- **canonical infinite two-partition with two bijections:** not claimed here.

## Provenance

Recovered from the 2026-09-02 Erdős #197 campaign and re-adjudicated during the 2026-09-13 omitted-family release court. Historical novelty is not asserted; the parity construction is the standard beautiful-array mechanism, published here because it is a clean mathematical child theorem and because its finite/infinite boundary is directly relevant to the parent problem.
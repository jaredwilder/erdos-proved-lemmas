# Erdős #156 — corrected maximal-Sidon blocking theorem

**Author:** Jared Wilder  
**Status:** corrected child theorem recovered from the campaign contradiction history  
**Parent problem:** not closed by this note

## Setup

Let `A ⊆ [N]` be a **full-convention Sidon set**: all sums `a+b` with `a,b∈A` and `a≤b` are distinct. Say `A` is inclusion-maximal in `[N]` if no `x∈[N]\A` can be adjoined while preserving the Sidon property.

For a set `A`, write

- `A+A-A = {b+c-a : a,b,c∈A}`;
- `(A+A)/2 = {x∈Z : 2x=b+c for some b,c∈A}`.

The midpoint term is load-bearing.

## Corrected theorem

For a full-convention Sidon set `A⊆[N]`,

```text
A is maximal in [N]
    iff
[N] ⊆ A ∪ (A+A-A) ∪ (A+A)/2.
```

### Proof

Fix `x∈[N]\A`.

If `A∪{x}` is not Sidon, a new collision must involve `x`. Apart from trivial equalities, there are two possibilities.

1. `x+a=b+c` for `a,b,c∈A`. Then `x=b+c-a∈A+A-A`.
2. `2x=b+c` for distinct `b,c∈A`. Then `x∈(A+A)/2`.

Conversely, either representation produces a collision between a sum involving the new point `x` and an old sum from `A`; because `x∉A`, the two unordered pairs are genuinely different. Thus every outside point is blocked exactly when the displayed covering holds.

## Why the older inclusion was false

An earlier campaign record omitted `(A+A)/2` and claimed

```text
[N] ⊆ A ∪ (A+A-A).
```

That is false for the canonical full Sidon convention.

Take

```text
N = 3,
A = {1,3},
x = 2.
```

`A` is Sidon and maximal: adjoining `2` creates

```text
1+3 = 2+2 = 4.
```

But

```text
(A+A)-A = {-1,1,3,5},
```

so `2` is not in `A ∪ (A+A-A)`. Its only obstruction is the midpoint collision `2x=1+3`.

This is a genuine correction, not a cosmetic rewrite.

## Corrected cubic counting bound

Let `m=|A|`. The corrected cover gives

```text
N ≤ |A ∪ (A+A-A) ∪ (A+A)/2|.
```

Using unordered old sums in `A+A`,

```text
|A+A-A| ≤ m * C(m+1,2) = m²(m+1)/2,
```

and only distinct pairs can create a midpoint outside `A`, so

```text
|(A+A)/2 \ A| ≤ C(m,2) = m(m-1)/2.
```

Hence

```text
N ≤ m + m²(m+1)/2 + m(m-1)/2
  = m + (m³ + 2m² - m)/2
  ≤ m + 2m³                  (m≥1).
```

In particular every maximal full-Sidon set satisfies the surviving lower-bound form

```text
|A| ≥ ((N-|A|)/2)^(1/3).
```

The campaign's earlier cubic lower-bound conclusion therefore survives, but **only through the corrected blocking identity**.

## Scope

This note does **not** provide the missing opposite-direction construction of maximal Sidon sets of size `O(N^(1/3))`. That construction problem remained open in the recovered campaign.

Historical novelty is not asserted. The point of this release is to preserve the exact surviving mathematics together with the counterexample that killed the stale formulation.

## Provenance

Recovered during the 2026-09-13 audit of the 97 omitted PROVED-bearing Erdős families. The later boundary audit explicitly retracted the midpoint-free inclusion and retained the corrected identity and cubic count.
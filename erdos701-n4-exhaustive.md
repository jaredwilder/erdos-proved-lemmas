# Erdős #701 — Chvátal star theorem holds on ground sets of size at most 4

Author: Jared Wilder. Public release: 2026-09-11.

## Theorem

Let `F` be a finite hereditary family of subsets of a ground set `X` with

`|X|<=4`.

Then every pairwise-intersecting subfamily of `F` has size at most a largest star of `F`.

Equivalently, Chvátal's hereditary-family star conjecture holds for every ground set of size at most 4.

## Verification

This is an exact finite theorem, verified by exhaustive enumeration.

The numbers of hereditary families/downsets are

- `3` on a 1-point ground set,
- `6` on 2 points,
- `20` on 3 points,
- `168` on 4 points.

For each of these `197` families, the verifier computes exactly:

1. the maximum size of a pairwise-intersecting subfamily, as a maximum clique in the intersection graph of the nonempty members;
2. the maximum star size;
3. the inequality between the two.

No violation occurs.

The standalone deterministic verifier is `verify_erdos701_n4.py`.

## Correction boundary

A Pass-6 summary described `4+16+256+65536=65812` objects as hereditary families. Those are instead the numbers of **all** families of subsets on ground sets of sizes 1 through 4. The actual hereditary-family count is `197`.

Semantic Court 14 records that accounting correction. The finite theorem itself survives independently.

## Scope

This is a complete finite theorem through `|X|=4`, not a proof for arbitrary ground-set size. A separate theorem in this repository proves the complete rank-at-most-2 hereditary case for arbitrary finite ground sets.
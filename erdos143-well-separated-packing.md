# Erdős #143 — packing bound for well-separated sets

Let `A ⊂ (1,∞)` satisfy the well-separation condition from Erdős #143. A five-theorem Lean development proves the finite packing estimate

\[
|A\cap(-\infty,2X)|\le \lceil X\rceil,
\]

and consequently

\[
|A\cap(-\infty,Y)|\le Y/2+1.
\]

The constant `1/2` is sharp for this packing method; the accompanying exact-arithmetic enumerator records an attaining family.

## Formal evidence

The source is preserved at
`jaredwilder/erdos-campaign-archive/campaigns/erdos143-close-2026-09-05/E143.lean`.

Its five recorded declarations are:

- `one_le_dist`
- `two_le_of_mem`
- `ncard_inter_Iio_le`
- `ncard_le_half`
- `wellSeparated_ncard_le`

The campaign receipt records successful Lean compilation and the axiom footprint

`[propext, Classical.choice, Quot.sound]`

for all five declarations, with no `sorryAx`.

The upstream Erdős predicate was transcribed into the campaign file; the campaign record classifies that binding as a transcription check rather than a kernel-checked equivalence to the upstream source file.

## Scope and literature status

This is an upper-density packing theorem. The deeper Erdős #143 questions concerning lower density and the relevant logarithmic summability statement are separate.

The campaign's literature audit suspected that the packing observation is classical/elementary, but did not execute a full prior-art search. Accordingly this file records the proved theorem without asserting historical novelty.

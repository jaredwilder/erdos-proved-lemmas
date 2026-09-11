# Erdős #949 — finite and countable sum-free avoidance theorems

**Author:** Jared Wilder  
**Recovered synthesis:** 2026-09-02  
**Human theorem-bank promotion:** 2026-09-11

Let `S⊆R` be sum-free: there are no `x,y,z∈S` with `x+y=z`.

This note records three exact partial results from the Erdős #949 program. The continuum-cardinality parent question is not assumed here.

## 1. Sharp finite constant

For every sum-free `S⊆R`, there exists

`q∈{1,2,3,4,5}`

such that both `q` and `2q` lie outside `S`. The constant 5 is best possible.

A short contradiction argument handles the two cases `1∈S` and `2∈S`; sharpness is witnessed by `S={1,4,6}`, for which every `q=1,2,3,4` has at least one of `q,2q` in `S`.

## 2. Complete countable analogue

Every sum-free `S⊆R` admits a countably infinite set

`A⊆N\S`

with

`A+A⊆R\S`.

Color the positive integers by membership in `S`. Hindman's theorem gives an infinite sequence whose finite-sums set is monochromatic. The monochromatic color cannot be “inside `S`,” because `x_1,x_2,x_1+x_2∈S` would contradict sum-freeness. Hence the entire finite-sums set avoids `S`.

## 3. Simultaneous finite-dilate IP avoidance

For every finite `D⊆R`, there is an infinite sequence `x_1,x_2,...∈N` such that for every `d∈D`,

`d FS(x_i) ∩ S = ∅`.

Color each `n` by the finite membership vector `(1_S(dn))_(d∈D)`. Hindman's theorem gives a monochromatic finite-sums set. Any coordinate equal to 1 would put `dx_1`, `dx_2`, and `d(x_1+x_2)` inside `S`, again contradicting sum-freeness.

## Formal evidence

The Lean theorem bank contains a substantial #949 formal group:

- `Erdos949Core.lean` — 4 declarations;
- `Erdos949Hindman.lean` — 13 declarations;
- `Erdos949HindmanFS.lean` — 16 declarations.

All 33 counted declarations are part of the clean formal core of `jaredwilder/erdos-theorems`, with the repository's recorded standard axiom footprint. The formalization includes the countable analogue and full finite-sums strengthening.

## Repository status

Thirty-three formal declarations plus the human finite/countable/IP theorem package make #949 large enough to graduate to a dedicated problem repository when one is initialized. Until then:

- ordinary mathematical reading: this file;
- Lean artifacts: `jaredwilder/erdos-theorems/theorems/erdos949-campaign-001/`;
- source/provenance: `jaredwilder/unpublished-math-papers/erdos949-sumfree-ip/`.

Historical novelty remains a separate literature question; Hindman's theorem itself is classical.

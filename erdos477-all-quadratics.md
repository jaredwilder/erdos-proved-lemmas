# Erdős #477 — all-quadratic direct-sum obstruction

Reader presentation prepared 2026-09-13.

This page records a complete written proof at the degree-2 scope. It is not a claim about degree `≥3`.

Let `f(x)=a x²+b x+c` be an integer quadratic with `a≠0`. There is no set `A⊆Z` such that

`A ⊕ f(Z) = Z`,

where `⊕` means every integer has exactly one representation as an ordered pair `(u,v)∈A×f(Z)`. Values of `f` are elements of a set; repeated polynomial preimages are not counted separately.

Let `B=f(Z)`. Choose an integer `t` with `c₀=2at+b≠0` (take `t=0` if `b≠0`, otherwise `t=1`). For every integer `x`,

`f(t+x)−f(t−x)=2c₀x`,

so `2c₀ Z ⊆ B−B`. If `A⊕B=Z`, two distinct elements of `A` cannot have a difference in `B−B`, since that would give two representations of the same integer. Therefore no two distinct elements of `A` are congruent modulo `2|c₀|`, and `A` is finite (indeed `|A|≤2|c₀|`).

If `a>0`, the image `B` is bounded below; if `a<0`, it is bounded above. Adding a finite set `A` preserves the corresponding one-sided bound, so `A+B` cannot equal all of `Z`. This contradiction proves the all-quadratic obstruction.

## Authority boundary

This written proof is not kernel-checked in the current public estate. The public [square-case Lean source](https://github.com/jaredwilder/erdos-theorems/blob/main/theorems/erdos477-campaign-001/Erdos477NoSquareTiling.lean) and its adjacent receipts cover the narrower square slice. See also the [written square obstruction](erdos477-square-tiling-obstruction.md). This page is a newly prepared written presentation, not a byte-for-byte recovery of a historical proof artifact. Later degree-`≥3` work is outside this page.

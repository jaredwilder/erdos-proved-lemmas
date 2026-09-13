# Erdős #289 — p-adic obstructions for integral reciprocal sums

Author: Jared Wilder. Public release: 2026-09-11.

## Theorem 1 — all-prime p-adic obstruction

Let `S` be a finite set of integers at least 2 and suppose

`sum_{n∈S} 1/n ∈ Z`.

Fix a prime `p` and define

`U_p = sum_{n∈S, p|n} p/n`.

Then

`v_p(U_p) >= 1`, using the convention `v_p(0)=+∞`.

### Proof

If `U_p=0`, the assertion is immediate. Otherwise write

`T = U_p/p + V_p`,

where every denominator occurring in `V_p` is prime to `p`. Hence `v_p(V_p)>=0`. Since `T` is an integer, `v_p(T)>=0`, so `U_p/p=T-V_p` is p-adically integral. Therefore `v_p(U_p)-1>=0`.

## Theorem 2 — one consecutive interval can never sum to an integer

Let

`a<a+1<...<b`

be a finite interval of positive integers with at least two terms. Then

`sum_{n=a}^b 1/n`

is not an integer.

### Proof

Inside any finite interval of at least two consecutive integers there is a unique element with maximal `v_2`.

Let `L=lcm(a,a+1,...,b)`. After clearing denominators,

`L sum_{n=a}^b 1/n = sum_{n=a}^b L/n`.

The term corresponding to the unique denominator with maximal `v_2` is odd, while every other term is even. Hence the cleared numerator is odd. But `L` is even. Therefore the reciprocal sum cannot be an integer.

## Theorem 3 — parity condition for a finite sum of interval sums

Suppose finitely many consecutive-integer blocks are added and the resulting reciprocal sum is an integer.

For each block, record the maximum `v_2` attained by a denominator in that block. Let `M` be the largest such level among all blocks, and assume `M≥1` (at least one denominator is even). The blocks consist of positive integers; occurrences are counted with multiplicity if blocks overlap.

Then **an even number of blocks must attain the global level `M`**.

### Proof

Clear the global least common multiple of all denominators. Within each block, exactly one term at that block's maximal `v_2` level contributes odd parity after the appropriate normalization. Blocks below the global level contribute even terms after clearing the global lcm; each block attaining the global level contributes one odd term. An integral total therefore requires an even number of such odd contributions.

## Further rigidity

A separate exact reduction for reciprocal-interval decompositions of 1 shows that if the denominator 2 occurs, its interval is forced to be `[2,3]`, leaving a tail of exactly `1/6`. A finite formal check rules out a single interval `[a,b]` with `5<=a<b<=60` summing to `1/6`.

## Scope

The all-prime and 2-adic parity theorems are unconditional. The `b<=60` tail obstruction is a finite statement and should be read at exactly that range.

Historical novelty is not claimed.

## Reader map and proof authority

The all-prime argument above is a written proof. The [formal campaign directory](https://github.com/jaredwilder/erdos-theorems/tree/main/theorems/erdos289-campaign-001) contains `Erdos289Head.lean`, two `msl_erdos289_a_m01` files, and their available axiom/verification records. Those are narrower head and finite-tail artifacts; they do not establish a kernel check of the entire all-prime theorem above. The finite tail range remains `5≤a<b≤60`.

Theorem 3 explicitly requires `M≥1`: without it, the single block `[1,1]` has integer sum and one block at level zero, contradicting the unqualified parity wording. This hypothesis clarification was added on 2026-09-13; it does not change the all-prime theorem or the interval theorem with at least two terms.

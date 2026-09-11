# Erdős #489 — exact finite-periodic squared-gap formula

Author: Jared Wilder  
Public release: 2026-09-11

Let `A` be a finite set of positive integers and

`B={n>=1 : a does not divide n for every a in A}`.

Assume `1 notin A`, so `B` is infinite. Put `M=lcm(A)`.

## Theorem

Membership in `B` is periodic modulo `M`. If

`1 <= r_1 < ... < r_t <= M`

are the surviving residues in one period and

`d_i=r_(i+1)-r_i` for `i<t`, `d_t=M+r_1-r_t`,

then for `B={b_1<b_2<...}`,

`lim_{x->infinity} (1/x) sum_{b_i<x} (b_(i+1)-b_i)^2`

exists and equals

`(1/M) sum_{i=1}^t d_i^2`.

## Proof

Because every `a in A` divides `M`, divisibility by every member of `A` depends only on the residue modulo `M`. Thus `B` is exactly periodic modulo `M`.

Across each complete period the successive gaps are the same cyclic list

`d_1,...,d_t`.

Up to `x`, the number of complete periods is `x/M+O(1)`. Hence

`sum_{b_i<x}(b_(i+1)-b_i)^2`

`= (x/M) sum_i d_i^2 + O(1)`,

where the boundary contributes only a bounded number of bounded periodic gaps. Division by `x` gives the stated limit.

If `1 in A`, then `B` is empty and the problem degenerates separately.

## Scope

This completely handles finite `A`. Erdős #489 asks about arbitrary sparse infinite `A`; the raw mine's attempted prime counterexample was false because taking `A` to be all primes leaves only `B={1}`.

## License

Apache-2.0.

# Erdős #85 — exact small values `f(5)=f(6)=f(7)=3`

Author: Jared Wilder. Public release: 2026-09-11.

Let `f(n)` be the least integer `d` such that every graph on `n` vertices with minimum degree at least `d` contains a 4-cycle `C4`.

## Theorem

For `n=5,6,7`,

`f(n)=3`.

For the lower bound, the cycle `C_n` is `C4`-free and has minimum degree 2.

For the upper bound, let `G` be `C4`-free and fix a vertex `v`. For distinct `u,w∈N(v)`, the sets `N(u)\{v}` and `N(w)\{v}` are disjoint, since a common vertex would create the 4-cycle `v-u-x-w-v`. Hence

`Σ_{u∈N(v)}(deg(u)-1) ≤ n-1`.

If `δ(G)≥3`, then `2 deg(v)≤n-1`. This is impossible for `n=5,6`; for `n=7` it forces every vertex to have degree exactly 3, contradicting the handshake lemma on seven vertices.

Thus every graph on 5, 6, or 7 vertices with minimum degree at least 3 contains a `C4`.

An exhaustive verifier independently confirms `f(4)=2`, `f(5)=f(6)=f(7)=3`. Historical priority is a separate literature question; these values are closely related to classical `R(C4,K_{1,n})` work.

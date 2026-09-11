# Erdős #566 — exact size-Ramsey endpoint rhat(K2,H)=e(H)

**Author:** Jared Wilder  
**Public routing:** 2026-09-11  
**Source:** Pass-3 non-PROVED route candidate; universal statement independently re-proved

Let `rhat(G,H)` denote the size-Ramsey number: the minimum number of edges of a graph `F` such that every red/blue edge-colouring of `F` contains a red copy of `G` or a blue copy of `H`.

## Theorem

For every finite graph `H`,

\[
\boxed{\hat r(K_2,H)=|E(H)|.}
\]

## Proof

### Upper bound

Take `F=H`. In any red/blue colouring of `F`, either some edge is red, which is already a red `K_2`, or no edge is red, in which case every edge is blue and the whole graph `H` is a blue copy of `H`.

Therefore

\[
\hat r(K_2,H)\le |E(H)|.
\]

### Lower bound

Let `F` have fewer than `|E(H)|` edges. Colour every edge of `F` blue. There is no red `K_2`. Also `F` cannot contain a copy of `H`, because any copy of `H` requires `|E(H)|` distinct edges while `F` has fewer.

Thus such an `F` does not arrow `(K_2,H)`, and

\[
\hat r(K_2,H)\ge |E(H)|.
\]

Combining the bounds proves equality.

## Scope

This closes the exact `G=K_2` endpoint. It does not provide the uniform linear bound for the broader fixed-`G` class in Erdős #566. The historical route correctly proved this endpoint but did not transfer it to the full problem.

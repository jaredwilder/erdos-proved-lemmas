# Erdős #1212 — infinitely many admissible dead ends

**Author:** Jared Wilder  
**Public release:** 2026-09-11  
**Status:** exact structural obstruction; parent path-existence problem remains open

Let `G` have as vertices the coprime pairs `(x,y) in N^2`; two vertices are adjacent when one coordinate changes by `+1` or `-1` and the other stays fixed.

The canonical question asks for a path going to infinity whose vertices satisfy both `min(x,y)>1` and the condition that at least one coordinate is composite.

## Theorem

For every integer `k>=2`, the vertex

`v_k=(2,3^k)`

is a vertex of `G` with exactly one neighbor in the full graph, namely

`(1,3^k)`.

Consequently `v_k` is **isolated in the admissible subgraph** cut out by `min(x,y)>1`.

Thus the admissible region contains infinitely many explicit dead ends.

## Proof

Since `3^k` is odd,

`gcd(2,3^k)=1`,

so `(2,3^k)` is a vertex of `G`.

Its only four possible coordinate-neighbors are

`(1,3^k)`, `(3,3^k)`, `(2,3^k-1)`, `(2,3^k+1)`.

Now:

- `gcd(1,3^k)=1`, so `(1,3^k)` is a graph neighbor;
- `gcd(3,3^k)=3`, so `(3,3^k)` is not a vertex;
- `3^k-1` is even, so `gcd(2,3^k-1)=2`;
- `3^k+1` is even, so `gcd(2,3^k+1)=2`.

Hence `(1,3^k)` is the unique neighbor in the full graph.

But that neighbor has minimum coordinate `1`, so it lies outside the admissible region `min(x,y)>1`. Therefore `(2,3^k)` has degree zero in the admissible subgraph.

Since the vertices `(2,3^k)` are distinct for all `k>=2`, this gives infinitely many admissible dead ends.

## Scope

An infinite family of isolated admissible vertices does not by itself rule out some other infinite admissible path. Erdős #1212 therefore remains open in this release.

The theorem is nevertheless a genuine global obstruction family, not finite-search evidence.

## License

Apache-2.0.

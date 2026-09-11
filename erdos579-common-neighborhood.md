# Erdős #579 — common neighborhoods are `K_{2,2}`-free

Author: Jared Wilder  
Public release: 2026-09-11

## Theorem

Let `G` be a graph containing no `K_{2,2,2}`. For **any two distinct vertices** `u,v`, the common neighborhood

`N(u) cap N(v)`

induces a `K_{2,2}`-free graph.

## Proof

Suppose the common neighborhood contained a `K_{2,2}` with bipartition

`{a,b}` and `{c,d}`.

Because all four vertices lie in `N(u) cap N(v)`, each of `u,v` is adjacent to each of `a,b,c,d`. The `K_{2,2}` supplies all four edges between `{a,b}` and `{c,d}`.

Therefore the six vertices with parts

`{u,v}`, `{a,b}`, `{c,d}`

contain a `K_{2,2,2}` subgraph, contradiction.

No assumption on whether `u` and `v` are adjacent is needed, since edges within a part are irrelevant to the existence of the complete tripartite subgraph.

## Scope

This is a local structural lemma inside Erdős #579. It does not by itself prove the canonical linear independent-set bound for dense `K_{2,2,2}`-free graphs.

The recovered promoted catalog stated the result only for a nonadjacent pair; reconstruction shows that restriction is unnecessary.

## License

Apache-2.0.

# Erdős #595 — countable-graph stratum

**Author:** Jared Wilder  
**Release:** 2026-09-11

Every countable graph is a countable union of triangle-free graphs.

## Proof

Enumerate the edge set as

\[
E(G)=\{e_1,e_2,\ldots\}
\]

(with a finite enumeration if the graph has finitely many edges). For each edge `e_i`, let `G_i` be the graph with the same vertex set and the single edge `e_i`. Every `G_i` is triangle-free, and

\[
G=\bigcup_i G_i.
\]

Thus any genuinely difficult witness to a formulation asking whether a graph can fail to be a countable union of triangle-free graphs must be uncountable.

## Scope boundary

This is a cardinality reduction, not a solution of the uncountable parent problem and not a novelty claim.

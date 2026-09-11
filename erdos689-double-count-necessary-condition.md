# Erdős #689 — double-count necessary condition

**Author:** Jared Wilder  
**Release:** 2026-09-11

Suppose that for each prime `p<=n` one chooses a residue class `a_p (mod p)`, and every integer in `[1,n]` is covered by at least two of the chosen classes. Then necessarily

\[
\boxed{
\sum_{p\le n}\left\lceil\frac np\right\rceil\ge2n.
}
\]

## Proof

A single residue class modulo `p` meets `[1,n]` in at most `ceil(n/p)` integers. Therefore the total number of incidences between integers in `[1,n]` and the chosen residue classes is at most

\[
\sum_{p\le n}\left\lceil\frac np\right\rceil.
\]

On the other hand, if every one of the `n` integers is covered at least twice, the same incidence count is at least `2n`. Comparing the two counts proves the inequality.

## Scope boundary

This is a necessary counting condition only. It is asymptotically too weak by itself to settle the parent covering problem; it is released as an exact reduction rather than a close.

# Erdős #655 — regular-polygon counterexample to the literal statement

**Author:** Jared Wilder  
**Status:** exact negative resolution of the literal statement; **independently rediscovered, not novel**  
**Known attribution:** Zach Hunter is credited by the current Erdős Problems page with the same equally-spaced-circle counterexample.

## Literal problem

Let `X={x_1,...,x_n}⊂R²` have the property that no circle centred at one of the `x_i` contains three other points of `X`. The literal question asks whether there is a constant `c>0` such that every sufficiently large valid `X` determines at least

\[
(1+c)\frac n2
\]

distinct pairwise distances.

The answer to the literal statement is **no**.

## Counterexample

Take the vertices of a regular `n`-gon on a circle of radius `R>0`:

\[
X_n=\{R e^{2\pi i j/n}:0\le j<n\}.
\]

For two vertices with cyclic separation `k`,

\[
d(k)=2R\sin\frac{\pi k}{n}.
\]

Because

\[
d(k)=d(n-k),
\]

and sine is strictly increasing on `(0,π/2]`, the nonzero distances are indexed exactly by

\[
k=1,2,\ldots,\left\lfloor\frac n2\right\rfloor.
\]

Hence

\[
\boxed{D(X_n)=\left\lfloor\frac n2\right\rfloor.}
\]

## Verification of the hypothesis

Fix a vertex `x_j`.

For every separation `k<n/2`, exactly two vertices lie at distance `d(k)` from `x_j`: the vertices at offsets `+k` and `-k` modulo `n`. If `n` is even, the antipodal distance `k=n/2` occurs once.

Therefore every positive-radius circle centred at any vertex contains at most two other vertices of `X_n`. The problem's hypothesis is satisfied for every `n≥3`.

Equivalently, equality of vertex distances satisfies

\[
d(k)=d(\ell)
\iff
k\equiv\pm\ell\pmod n.
\]

## Literal negation

For every `c>0` and every `n≥3`,

\[
D(X_n)=\left\lfloor\frac n2\right\rfloor
\le \frac n2
< (1+c)\frac n2.
\]

Thus the regular polygons give counterexamples for unbounded `n`—indeed for every `n≥3`—and no positive constant `c` can satisfy the literal conjecture.

## Historical / novelty court

This construction was recovered independently in the Wilder estate during the 2026 Erdős mining campaigns. A current literature/status check shows it is **already known**:

- the Erdős Problems page for #655 explicitly credits **Zach Hunter** with observing that `n` equally spaced points on a circle disprove the conjecture;
- the current Formal Conjectures source also records the literal problem as solved negatively by the regular `n`-gon and keeps a strengthened general-position variant open.

Accordingly this file makes **no originality or priority claim** for the counterexample. It belongs in the public estate because it is a genuine independently rediscovered closure and because the estate's campaign reached the correct exact construction before the release audit reconciled it with current prior art.

## What remains open

The obvious intended repair is to impose stronger general-position assumptions, e.g. restrictions excluding the regular polygon. The current Formal Conjectures source includes such a general-position variant as open.

This note closes only the **literal frozen statement** above.

## Provenance

The estate's later certifier reconstructed the full-domain argument: all `n≥3`, every vertex centre, every radius `r>0`, exact chord classes `{k,n-k}`, and exactly `floor(n/2)` distinct distances. Finite replays through hundreds of `n` were corroboration; the proof is the analytic chord-class argument above.
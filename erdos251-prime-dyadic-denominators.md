# Erdős #251 — exact denominators of the prime dyadic partial sums

**Author:** Jared Wilder  
**Status:** all-`N` child theorem; parent irrationality question remains open in this estate

## Origin-zero formulation

Let `p_j` denote the `j`-th prime with `p_0=2`, `p_1=3`, and define the `N`-term partial sum

\[
S_N=\sum_{j=0}^{N-1}\frac{p_j}{2^j}.
\]

Then the lowest-terms denominator of `S_N` is

\[
\operatorname{den}(S_N)=
\begin{cases}
1,&N=1,\\
2^{N-1},&N\ge2.
\end{cases}
\]

## Proof

Put the sum over the common denominator `2^(N-1)`:

\[
S_N=\frac{M_N}{2^{N-1}},\qquad
M_N=\sum_{j=0}^{N-1}p_j\,2^{N-1-j}.
\]

For `N≥2`, every term with `j<N-1` is even. The final term is `p_{N-1}`, which is an odd prime. Therefore

\[
M_N\equiv p_{N-1}\equiv1\pmod2.
\]

So `M_N` is odd and no factor of `2` cancels. The denominator is exactly `2^(N-1)`.

At `N=1`, `S_1=p_0=2`, so the denominator is `1`.

## One-indexed equivalent

If instead `p_1=2,p_2=3,...` and

\[
T_N=\sum_{j=1}^{N}\frac{p_j}{2^j},
\]

then

\[
\operatorname{den}(T_1)=1,\qquad
\operatorname{den}(T_N)=2^N\quad(N\ge2).
\]

This is the same parity argument under the shifted indexing convention. The distinction matters because both conventions occurred in the recovered campaign records.

## What this does not prove

The frozen parent target asks about irrationality of the infinite series

\[
\sum_{j\ge0}\frac{p_j}{2^j}
\]

in the campaign's origin-zero convention.

Unbounded powers of two in the denominators of partial sums do **not by themselves** prove that the limit is irrational. A separate tail/transference argument is required. The recovered campaign explicitly lacked such a theorem and kept the irrationality target open.

Several earlier route ideas based on reading binary digits directly were killed by carry propagation; this denominator theorem survives those kills because it is only a finite exact parity statement for every `N`.

## Evidence boundary

The all-`N` proof above is elementary. The recovered estate also replayed the identity by exact `Fraction` arithmetic through finite ranges (including `N≤10` and `N≤25`), but those computations are corroboration rather than the reason the theorem holds.

Historical novelty is not asserted.
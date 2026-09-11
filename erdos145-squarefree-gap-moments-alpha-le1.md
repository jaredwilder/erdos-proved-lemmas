# Erdős #145 — squarefree-gap moments for `0 <= alpha <= 1`

**Author:** Jared Wilder  
**Public release:** 2026-09-11  
**Status:** mathematically audited, citation-dependent partial theorem

Let

`s_1 < s_2 < ...`

be the squarefree numbers and put `g_n=s_{n+1}-s_n`. Erdős #145 asks whether, for every `alpha>=0`, the limit

`(1/x) * sum_{s_n <= x} g_n^alpha`

exists.

## Theorem

For every fixed `alpha` with

`0 <= alpha <= 1`,

the requested limit exists. At `alpha=1` the limit is exactly `1`.

At `alpha=0` the limit is the squarefree density `6/pi^2`.

## External input

For every fixed integer gap `g`, the natural density of occurrences of the exact squarefree gap `g` exists. This is a standard fixed-pattern squarefree-correlation / Mirsky-type input. This note does not claim that input as new.

The proof below shows that this fixed-gap input is enough for the entire interval `0<=alpha<=1`; no bounded-gap hypothesis is used.

## Proof for `0 <= alpha < 1`

Fix `G>=1` and split the normalized moment into gaps `g_n<=G` and gaps `g_n>G`.

For the finitely many values `g<=G`, the external fixed-gap density theorem gives a limit term by term.

For the tail, since `alpha-1<0`, every `g>G` satisfies

`g^alpha <= G^(alpha-1) g`.

Therefore

`sum_{s_n<=x, g_n>G} g_n^alpha`

is at most

`G^(alpha-1) * sum_{s_n<=x} g_n`.

If `N=N(x)` is the largest index with `s_N<=x`, then the full gap sum telescopes:

`sum_{n<=N} g_n = s_{N+1}-s_1 = s_{N+1}-1`.

The squarefree numbers have positive natural density, so `s_{N+1}/x -> 1`. Hence, after division by `x`, the tail has limsup at most

`G^(alpha-1)`.

Letting `G->infinity` makes this bound tend to zero. Thus the finite-gap limiting sums are Cauchy in the cutoff and the full normalized moment has a limit.

## Endpoint `alpha=1`

The same telescoping identity gives directly

`(1/x) * sum_{s_n<=x} g_n = (s_{N+1}-1)/x -> 1`.

Hence the limit is exactly `1`.

## Endpoint `alpha=0`

Here every gap contributes `1`, so the normalized sum is simply the squarefree counting function divided by `x`, which tends to `6/pi^2`.

## Scope and correction history

This proves the interval `0<=alpha<=1`; it does **not** settle `alpha>1`.

A later archived route incorrectly asserted that squarefree gaps were bounded by `{1,2,3,4}`. That statement is false: CRT gives arbitrarily long runs of non-squarefree integers. The theorem above survives because its tail estimate uses telescoping, not bounded gaps.

Historical novelty is not claimed. The useful release is the clean reduction showing that standard fixed-gap densities already settle the full subcritical interval through `alpha=1`.

## License

Apache-2.0.

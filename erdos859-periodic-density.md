# Erdős #859 — the density exists and is rational for every fixed target

**Author:** Jared Wilder  
**Public release:** 2026-09-11  
**Status:** exact structural theorem; asymptotic parent problem remains open

For fixed `t>=1`, let `d_t` denote the density of integers `n` for which `t` can be represented as a sum of distinct positive divisors of `n`.

The canonical Erdős #859 problem asks for the asymptotic behaviour of `d_t` as `t->infinity`.

## Theorem

For every fixed positive integer `t`, the defining predicate is periodic in `n` with period

`L_t = lcm(1,2,...,t)`.

Consequently `d_t` always exists and is rational.

## Proof

If

`t = d_1 + ... + d_r`

is a sum of distinct positive divisors of `n`, then every `d_i<=t`. Thus the truth of the representation predicate depends only on which integers `d` in `{1,...,t}` divide `n`.

For every such `d`, we have `d | L_t`. Hence

`n ≡ n' (mod L_t)  =>  (d|n iff d|n')`

for every `1<=d<=t`.

Therefore the entire finite divisor-incidence pattern relevant to representations of `t` is determined by `n mod L_t`. The predicate is periodic modulo `L_t`.

A periodic subset of the positive integers has natural density equal to the number of successful residue classes divided by the period. Hence `d_t` exists and belongs to `Q`.

## Corrected small values

Independent exact residue enumeration in the recovered estate gives:

| `t` | `d_t` |
|---:|:---|
| 1 | 1 |
| 2 | 1/2 |
| 3 | 2/3 |
| 4 | 1/2 |
| 5 | 7/15 |
| 6 | 7/15 |
| 7 | 16/35 |
| 8 | 3/7 |
| 9 | 17/45 |
| 10 | 2/5 |
| 11 | 13/33 |
| 12 | 43/99 |

Several earlier campaign-local small values were inconsistent; this table is the corrected one preserved by the final audit.

## Scope

This theorem proves existence and rationality of every individual `d_t`. It does **not** determine the asymptotic law in `t`, in particular it does not prove

`d_t ~ c_1/(log t)^c_2`.

Historical novelty is not claimed; the periodicity mechanism is elementary. Its value is to remove density existence as a hidden issue and leave the parent problem purely asymptotic.

## License

Apache-2.0.

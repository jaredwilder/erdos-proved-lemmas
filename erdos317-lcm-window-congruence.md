# Erdős #317 — repaired LCM-window congruence

**Author:** Jared Wilder  
**Status:** elementary theorem + correction of a false predecessor

Let

\[
L_n=\operatorname{lcm}(1,2,\ldots,n).
\]

Let `p` be a prime satisfying

\[
\frac n2<p\le n,
\]

and let `δ_1,...,δ_n` be arbitrary integers. Then

\[
\boxed{
\sum_{k=1}^n \delta_k\frac{L_n}{k}
\equiv
\delta_p\frac{L_n}{p}
\pmod p.
}
\]

The recovered campaign stated the result only for `δ_k in {-1,0,1}`. The same proof gives arbitrary integer coefficients.

## Proof

Because `p<=n`, the prime `p` divides `L_n`.

Since `p>n/2`, the only multiple of `p` among `1,...,n` is `p` itself. Therefore for every `k!=p`, the integer `k` contains no factor `p`, while `L_n` contains one copy of every prime-power contribution needed up to `n`; in particular

\[
p\mid \frac{L_n}{k}.
\]

Hence every summand with `k!=p` vanishes modulo `p`, leaving exactly

\[
\delta_p\frac{L_n}{p}.
\]

This proves the congruence. ∎

## The older form is false

An earlier route replaced the right-hand side by

\[
\delta_p L_{p-1}.
\]

That is not generally congruent to `δ_p L_n/p` modulo `p`.

Take all coefficients zero except `δ_p=1`.

### `n=7`, `p=5`

\[
L_7=420,
\qquad
\frac{L_7}{5}=84\equiv4\pmod5,
\]

whereas

\[
L_4=12\equiv2\pmod5.
\]

### `n=10`, `p=7`

\[
L_{10}=2520,
\qquad
\frac{L_{10}}7=360\equiv3\pmod7,
\]

whereas

\[
L_6=60\equiv4\pmod7.
\]

Thus the `L_{p-1}` version is refuted by exact small counterexamples, while the `L_n/p` version holds uniformly.

## Scope

This is a repaired local congruence tool from the #317 campaign. It is not by itself a resolution of the parent Erdős problem. Any downstream route must use the repaired form rather than the falsified `L_{p-1}` substitution.

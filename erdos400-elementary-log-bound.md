# Erdős #400 — elementary logarithmic upper bound and factorial-subsequence scale

**Author:** Jared Wilder  
**Public release:** 2026-09-11  
**Pass-3 asymptotic upgrade:** 2026-09-11

For fixed `k>=2`, let `g_k(n)` be the maximum of

\[
a_1+\cdots+a_k-n
\]

over tuples satisfying

\[
a_1!\cdots a_k!\mid n!.
\]

## Theorem 1 — elementary pointwise upper bound

For every `n>=1`,

\[
\boxed{g_k(n)\le k(\lfloor\log_2n\rfloor+1).}
\]

### Proof

Any admissible `a_i` satisfies `a_i<=n`, since `a_i!|n!` is impossible for `a_i>n`.

Let `s_2(r)` be the sum of the binary digits of `r`. Legendre's formula gives

\[
v_2(r!)=r-s_2(r).
\]

Divisibility of the factorial product implies

\[
\sum_i(a_i-s_2(a_i))\le n-s_2(n).
\]

Hence

\[
\sum_i a_i-n
\le
\sum_i s_2(a_i)-s_2(n)
\le
\sum_i s_2(a_i)
\le
k(\lfloor\log_2n\rfloor+1).
\]

Taking the maximum proves the bound.

## Theorem 2 — explicit factorial subsequence

For every integer `m>=2`, putting `n=m!` gives

\[
\boxed{g_k(m!)\ge m+k-3.}
\]

### Proof

Choose

\[
(a_1,\ldots,a_k)=(m!-1,m,1,\ldots,1).
\]

Then

\[
(m!-1)!\,m!=(m!)!,
\]

so the tuple is admissible for argument `n=m!`. Its excess is

\[
(m!-1)+m+(k-2)-m!=m+k-3.
\]

## Theorem 3 — Pass-3 asymptotic interpretation

Along the factorial subsequence `n=m!`,

\[
\boxed{
g_k(n)
\ge
(1+o(1))\frac{\log n}{\log\log n}.
}
\]

Consequently the elementary package gives the scale sandwich

\[
\boxed{
\Omega_k\!\left(\frac{\log n}{\log\log n}\right)
\text{ infinitely often},
\qquad
g_k(n)=O_k(\log n).
}
\]

### Proof

Stirling gives

\[
\log(m!)=m\log m-m+O(\log m),
\]

and therefore

\[
m=(1+o(1))\frac{\log n}{\log\log n}
\qquad(n=m!).
\]

Insert this into Theorem 2; the additive constant `k-3` is negligible.

## Literature boundary

The logarithmic pointwise order is classical: Erdős and Graham explicitly record that `g_k(n) <<_k log n` is easy. A 2026 paper of Eric Li gives a sharper pointwise upper bound and a density-one logarithmic lower bound. This file makes **no historical novelty claim** for that order of magnitude.

The release preserves the exact digit-sum derivation, the explicit factorial family, and the consequent subsequence scale in one auditable place. The parent asymptotic questions remain separate.

## License

Apache-2.0.

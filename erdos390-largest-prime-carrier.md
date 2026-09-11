# Erdős #390 — factorial envelope and lower bounds

**Author:** Jared Wilder  
**Public release:** 2026-09-11  
**Pass-3 promotion:** 2026-09-11

Consider an admissible factorization in the frozen nontrivial branch

\[
n!=a_1a_2\cdots a_k,
\qquad
n<a_1<\cdots<a_k=m,
\]

with the route's admissibility conditions.

## Theorem 1 — factorial envelope

Every such factorization satisfies

\[
\boxed{(n!)^2\le m!.}
\]

### Proof

The selected factors `a_i` are distinct integers in the interval `(n,m]`. Their product is `n!`. Hence their product is at most the product of **all** integers in that interval:

\[
n!=\prod_i a_i
\le
\prod_{j=n+1}^{m}j
=
\frac{m!}{n!}.
\]

Multiply by `n!`.

## Corollary 2 — asymptotic lower envelope

Stirling inversion of

\[
\log(m!)\ge2\log(n!)
\]

gives

\[
\boxed{
m\ge
2n-(2\log2+o(1))\frac{n}{\log n}.}
\]

Thus the extremal largest factor satisfies the same one-sided lower bound whenever the frozen function is defined.

### Constant check

Write

\[
m=2n-d\frac n{\log n}.
\]

Using `log(t!)=t log t-t+O(log t)` and expanding around `2n`,

\[
\log(m!)-2\log(n!)
=
(2\log2-d)n+o(n).
\]

Therefore `(n!)^2<=m!` forces asymptotically `d<=2log2`, which is exactly the displayed lower envelope.

## Theorem 3 — largest-prime carrier

Let `p_*(n)` be the largest prime at most `n`. If `p_*(n)>n/2`, every admissible factorization satisfies

\[
\boxed{m\ge2p_*(n).}
\]

Indeed `v_p(n!)=1` for `p=p_*(n)>n/2`, so some selected factor is divisible by `p`. Since every selected factor exceeds `n`, that factor is at least the first multiple of `p` above `n`, namely at least `2p`.

## Correction boundary

The campaign also explored stronger claims intended to identify the full asymptotic constant. Those bridges were killed. In particular:

- the pointwise assertion `f(n)>=2n` is false (`n=6` is an exact counterexample in the archived computation);
- no matching upper bound is supplied by the factorial envelope;
- the one-sided theorem above does **not** determine the canonical asymptotic constant.

This file publishes the surviving exact lower-side mathematics only.

## Formalization status

The Pass-4 Lean handoff identifies `(n!)^2<=m!` as a priority formalization target. It is **not** labelled kernel-checked here absent a green receipt.

## License

Apache-2.0.

# Erdős #486 — summable forbidden mass gives quantitative natural density

**Author:** Jared Wilder  
**Public release:** 2026-09-11  
**Pass-2 quantitative upgrade:** 2026-09-11

For each positive integer `n`, let `X_n` be a set of residue classes modulo `n`. A positive integer `m` survives when its residue avoids `X_n` for every activated modulus `n<m`. Let `B` be the set of survivors.

The activation threshold `n<m` is part of the theorem and is load-bearing.

## Theorem 1 — ordinary natural density

If

\[
\boxed{\sum_{n\ge1}\frac{|X_n|}{n}<\infty,}
\]

then `B` has an ordinary natural density. Consequently it has logarithmic density.

## Proof

Let `B_N` impose only restrictions with `n<=N`. Finitely many congruence restrictions with finite activation thresholds make `B_N` eventually periodic, so it has a natural density `delta_N`. The sets decrease with `N`, hence `delta_N` decreases to some `delta_*`.

Up to `x`, only moduli `N<n<x` can remove points of `B_N` that survive the first `N` restrictions. A modulus `n` removes at most

\[
|X_n|\left(\frac xn+1\right)
\]

integers up to `x`. Thus

\[
\frac{|(B_N\setminus B)\cap[1,x]|}{x}
\le
\sum_{N<n<x}\frac{|X_n|}{n}
+
\frac1x\sum_{N<n<x}|X_n|.
\]

The first term is bounded by the convergent tail. For the second, convergence of `sum |X_n|/n` and Kronecker's lemma give

\[
\frac1x\sum_{n\le x}|X_n|\to0.
\]

Therefore

\[
\delta_N-\sum_{n>N}\frac{|X_n|}{n}
\le
\underline d(B)
\le
\overline d(B)
\le
\delta_N.
\]

Letting `N->infinity` forces both densities to equal `delta_*`.

## Theorem 2 — certified truncation error

Put

\[
T_N=\sum_{n>N}\frac{|X_n|}{n}.
\]

Then every finite periodic truncation gives a rigorous density approximation:

\[
\boxed{0\le\delta_N-d(B)\le T_N.}
\]

So if the tail mass is explicitly bounded, the exact finite periodic density `delta_N` comes with an explicit deterministic error bar.

## Theorem 3 — positive-density regime

For each truncation, the union bound gives

\[
\delta_N\ge1-\sum_{n\le N}\frac{|X_n|}{n}.
\]

Combining this with the tail estimate and taking `N->infinity` yields

\[
\boxed{
d(B)\ge
\max\left(0,1-\sum_n\frac{|X_n|}{n}\right).
}
\]

In particular,

\[
\boxed{
\sum_n\frac{|X_n|}{n}<1
\Longrightarrow
d(B)>0.
}
\]

Thus the theorem gives not only existence of density but also certified finite approximation and a simple positive-density criterion.

## Supersession / #25 corollary

The earlier singleton-residue theorem used in the #25 campaign is a special case of this arbitrary-forbidden-set result. It should be cited as a corollary rather than maintained as a competing headline theorem.

## Scope and novelty

This proves the exact summable-forbidden-mass slice of Erdős #486, not the unrestricted parent problem. Historical novelty is not claimed without a specialist Davenport–Erdős / sieve-literature search; the quantitative formulation is published here as an audited mathematical consequence of the estate.

## License

Apache-2.0.

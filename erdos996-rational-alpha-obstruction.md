# Erdős #996 — an exact rational-α obstruction to pointwise strengthening

**Author:** Jared Wilder  
**Status:** exact child negative theorem / scope obstruction  
**Parent problem:** the almost-everywhere statement remains open in this estate

## Canonical context

Erdős #996 asks, under a Fourier-tail hypothesis on `f∈L²([0,1])` and for a lacunary sequence `n_k`, whether

\[
\frac1N\sum_{k\le N} f(\{\alpha n_k\})
\longrightarrow
\int_0^1f(x)\,dx
\]

for **almost every** `α`.

The almost-everywhere qualifier is load-bearing. It cannot be strengthened to every `α`, even for an extremely smooth test function and the simplest lacunary sequence.

## Exact obstruction

Take

\[
n_k=2^k,
\qquad
f(x)=e^{2\pi i x},
\qquad
\alpha=\frac17.
\]

The function `f` is a single Fourier mode. Hence its Fourier-tail error is eventually exactly zero, so it satisfies any decay hypothesis of the form appearing in the problem.

Also

\[
\int_0^1 e^{2\pi i x}\,dx=0.
\]

Let

\[
\zeta=e^{2\pi i/7}.
\]

Since powers of `2` modulo `7` cycle

\[
1,2,4,1,2,4,\ldots,
\]

the sampled sequence is periodic:

\[
f(\{2^k/7\})\in\{\zeta,\zeta^2,\zeta^4\}
\]

with period three. Therefore

\[
\lim_{N\to\infty}
\frac1N\sum_{k=1}^{N} f(\{2^k/7\})
=
\frac{\zeta+\zeta^2+\zeta^4}{3}.
\]

This limit is nonzero.

## Exact algebra

Put

\[
s=\zeta+\zeta^2+\zeta^4.
\]

Using `1+ζ+ζ²+⋯+ζ⁶=0`, let

\[
t=\zeta^3+\zeta^5+\zeta^6=-1-s.
\]

Then

\[
\begin{aligned}
s^2
&=(\zeta+\zeta^2+\zeta^4)^2\\
&=(\zeta+\zeta^2+\zeta^4)
   +2(\zeta^3+\zeta^5+\zeta^6)\\
&=s+2(-1-s)\\
&=-s-2.
\end{aligned}
\]

Hence

\[
\boxed{s^2+s+2=0}.
\]

In particular `s≠0`, and therefore the Cesàro limit is not the integral of `f`.

For the chosen root with positive imaginary part,

\[
s=\frac{-1+i\sqrt7}{2},
\qquad
\frac{s}{3}=\frac{-1+i\sqrt7}{6}.
\]

The nonzero conclusion requires only the quadratic identity, not this explicit radical form.

## Correction to the recovered campaign certificate

A historical campaign row stated

```text
ζ + ζ² + ζ⁴ = -1
```

and therefore claimed the limit was `-1/3`.

That exact value is false. The polynomial

```text
x³+x²-2x-1
```

belongs to the real cyclotomic quantities `2cos(2πj/7)`; it does not have `ζ,ζ²,ζ⁴` themselves as its three roots.

The underlying obstruction nevertheless survives unchanged because

\[
\zeta+\zeta^2+\zeta^4\ne0.
\]

This note supersedes the incorrect `-1/3` value wherever it appears in the recovered ledger.

## General rational mechanism

More generally, for rational `α=a/q` with odd `q`, the sequence `2^k mod q` is eventually periodic (indeed periodic on the unit orbit when `gcd(a,q)=1`). For a Fourier character `e^{2πix}`, the Cesàro limit is the average of the corresponding roots of unity over that finite orbit. Whenever that orbit average is nonzero, one gets the same pointwise obstruction.

The `q=7` example is simply an exact minimal-looking witness.

## What this does not prove

A single rational `α` is a measure-zero exceptional point. Therefore this theorem does **not** refute the canonical “for almost every `α`” assertion of Erdős #996.

It proves only that:

- the almost-everywhere qualifier cannot be dropped;
- pointwise-for-all-`α` variants are false;
- and any proof of the canonical statement must genuinely use a measure-theoretic mechanism rather than pointwise convergence.

Historical novelty is not asserted.
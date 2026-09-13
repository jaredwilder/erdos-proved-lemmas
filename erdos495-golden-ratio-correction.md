# Erdős #495 / Littlewood — correction of the golden-ratio diagonal claim

**Author:** Jared Wilder  
**Status:** exact correction / refutation of a false recovered lemma  
**Parent problem:** Littlewood's conjecture remains open in general

The canonical problem asks whether, for all real `alpha,beta`,

\[
\liminf_{n\to\infty} n\,\|n\alpha\|\,\|n\beta\|=0.
\]

A recovered campaign row asserted the opposite on the diagonal

\[
\alpha=\beta=\varphi=\frac{1+\sqrt5}{2},
\]

claiming

\[
\liminf_{n\to\infty} n\,\|n\varphi\|^2>0.
\]

That lemma is false.

## Where the archived argument fails

The row invokes bad approximability of the golden ratio:

\[
\|n\varphi\|\ge \frac{c}{n}
\]

for some fixed `c>0`.

Squaring and multiplying by `n` gives only

\[
n\|n\varphi\|^2\ge \frac{c^2}{n},
\]

whose lower bound tends to zero. It does **not** imply a positive lower bound for the liminf.

## Exact Fibonacci subsequence

Let `F_j` be the Fibonacci numbers with `F_1=F_2=1`. The standard Binet identity gives

\[
F_j\varphi-F_{j+1}=(-1)^{j+1}\varphi^{-j}.
\]

Hence

\[
\|F_j\varphi\|=\varphi^{-j}.
\]

Taking `n=F_j`,

\[
n\|n\varphi\|^2
=F_j\varphi^{-2j}.
\]

Since

\[
F_j=\frac{\varphi^j-(-\varphi)^{-j}}{\sqrt5},
\]

we obtain

\[
F_j\varphi^{-2j}
=\frac{\varphi^{-j}-(-1)^j\varphi^{-3j}}{\sqrt5}
\longrightarrow0.
\]

The expression is nonnegative, therefore

\[
\boxed{\liminf_{n\to\infty} n\|n\varphi\|^2=0.}
\]

So the golden-ratio diagonal is not a counterexample to Littlewood; it satisfies the conjectured conclusion along the Fibonacci denominators.

## Estate integrity consequence

The recovered corpus contains a `PROVED` row asserting the false positive-liminf claim, alongside other rows correctly treating the general problem as open. The `PROVED` label on that row must therefore not be propagated into theorem catalogs without semantic review.

This correction does not prove the full two-parameter Littlewood conjecture. It removes one false negative example and records an exact subsequence proof for the diagonal pair `(phi,phi)`.

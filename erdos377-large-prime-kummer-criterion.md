# Erdős #377 — corrected large-prime Kummer interval criterion

**Author:** Jared Wilder  
**Status:** exact structural theorem / corrected child criterion; parent boundedness problem remains open  
**Historical novelty:** not asserted

## Theorem

Let `p<=n` be prime and assume

\[
p>\sqrt{2n}.
\]

Put

\[
k=\left\lfloor\frac np\right\rfloor.
\]

Then

\[
\boxed{
p\nmid {2n\choose n}
\iff
p>\frac{2n}{2k+1}.
}
\]

Equivalently, within the large-prime regime `p>sqrt(2n)`, the primes failing to divide the central binomial coefficient are cut out by an exact interval condition determined by `k=floor(n/p)`.

## Proof

Write

\[
n=kp+r,
\qquad 0\le r<p.
\]

Since `p>sqrt(2n)`,

\[
p^2>2n.
\]

In particular `n<p^2`, so the base-`p` expansion of `n` has at most two digits, namely

\[
n=(k,r)_p.
\]

Moreover

\[
2k\le \frac{2n}{p}<p.
\]

Thus doubling the high digit `k` cannot create a base-`p` carry.

By Kummer's theorem, `v_p(C(2n,n))` equals the number of carries when adding `n+n` in base `p`. In the present two-digit regime, the only possible carry is therefore from the low digit `r`. Hence

\[
p\nmid {2n\choose n}
\iff
2r<p.
\]

Substituting `r=n-kp`,

\[
2(n-kp)<p
\iff
2n<(2k+1)p
\iff
p>\frac{2n}{2k+1}.
\]

This proves the criterion.

## Why the large-prime hypothesis matters

Without `p>sqrt(2n)`, the base-`p` expansion can have additional digits and carries can occur above the units digit. Several historical route statements tried to promote a one-digit or one-band condition beyond the regime where those higher carries are excluded; those stronger statements acquired counterexamples.

The theorem above is the repaired exact scope.

## Boundary

The frozen #377 campaign asks a stronger global boundedness/asymptotic question involving the primes that fail to divide `C(2n,n)`. This large-prime interval criterion is a structural decomposition of one regime only. It does not by itself settle the parent problem.

No novelty claim is made.
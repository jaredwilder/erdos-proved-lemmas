# Erdős #700 — exact prime-power binomial gcd identity

**Author:** Jared Wilder  
**Public routing:** 2026-09-11  
**Source:** Pass-3 promoted theorem, independently rechecked

Let `p` be prime, `a>=1`, and `0<k<p^a`.

## Theorem

\[
\boxed{
v_p\!\binom{p^a}{k}=a-v_p(k)
}
\]

and therefore

\[
\boxed{
\gcd\!\left(p^a,{p^a\choose k}\right)
=p^{a-v_p(k)}
=\frac{p^a}{\gcd(p^a,k)}.
}
\]

## Proof

Use

\[
{p^a\choose k}=\frac{p^a}{k}{p^a-1\choose k-1}.
\]

It remains to show that

\[
{p^a-1\choose k-1}
\]

is a `p`-adic unit. In base `p`, the number `p^a-1` has all `a` digits equal to `p-1`. Lucas's theorem therefore gives

\[
{p^a-1\choose k-1}\not\equiv0\pmod p
\]

for every `0<k<p^a`, because every base-`p` digit of `k-1` is at most `p-1`.

Hence all `p`-adic valuation comes from `p^a/k`, giving

\[
v_p\!\binom{p^a}{k}=a-v_p(k).
\]

Since `k<p^a`, one has `v_p(k)<a`, and the gcd formula follows.

## Corollary for the campaign minimum

For

\[
f(n)=\min_{1<k\le n/2}\gcd\!\left(n,{n\choose k}\right),
\]

whenever the domain is nonempty and `n=p^a` is a prime power with `n>=4`,

\[
\boxed{f(p^a)=p.}
\]

If `a>=2`, choose `k=p^{a-1}`, which lies in the allowed range and gives gcd `p`; no smaller positive power of `p` can occur. If `a=1` and `p>=5`, every allowed `k` has `v_p(k)=0`, so every gcd equals `p`.

## Relation to the semiprime theorem

The separate released theorem gives `f(pq)=p` for primes `p<=q`. Together, these provide exact prime-power and semiprime strata of the same binomial-gcd function.

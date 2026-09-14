# Erdős #700 — exact prime-power and semiprime binomial-gcd formulas

**Author:** Jared Wilder  
**Public release:** 2026-09-14

For the campaign quantity

\[
f(n)=\min_{1<k\le n/2}\gcd\!\left(n,{n\choose k}\right),
\]

this note records two exact families and a correction to a poisoned historical registry row.

## Theorem 1 — prime powers

Let `p` be prime, `a>=1`, and `0<k<p^a`. Then

\[
\boxed{
v_p\!\binom{p^a}{k}=a-v_p(k).
}
\]

Consequently

\[
\boxed{
\gcd\!\left(p^a,{p^a\choose k}\right)
=\frac{p^a}{\gcd(p^a,k)}.
}
\]

For `a>=2`, under the displayed definition of `f`,

\[
\boxed{f(p^a)=p.}
\]

### Proof

Use

\[
{p^a\choose k}
=\frac{p^a}{k}{p^a-1\choose k-1}.
\]

The base-`p` digits of `p^a-1` are all `p-1`. Therefore Lucas's theorem gives

\[
{p^a-1\choose k-1}\not\equiv0\pmod p,
\]

because every base-`p` digit of `k-1` is at most `p-1`. Thus the second factor is a `p`-adic unit and

\[
v_p\!\binom{p^a}{k}=a-v_p(k).
\]

Since `0<k<p^a`, one has `v_p(k)<=a-1`, giving the gcd identity.

For `a>=2`, every admissible `k` has gcd at least `p`, while `k=p^{a-1}` is admissible and gives gcd exactly `p` (including the endpoint `k=n/2` when `p=2`). Hence `f(p^a)=p`.

## Theorem 2 — semiprimes

Let `p<=q` be primes and set `n=pq`. Then

\[
\boxed{f(pq)=p.}
\]

This includes the square case `p=q`.

### Lower bound

The identity

\[
k{n\choose k}=n{n-1\choose k-1}
\]

implies

\[
\frac{n}{\gcd(n,{n\choose k})}\mid k.
\]

If `p<q`, the gcd can only be `1,p,q,pq`. It cannot be `1`, because that would force `n|k`, impossible for `1<k<=n/2`. Therefore every admissible gcd is at least `p`.

For `p=q`, the prime-power theorem gives the same lower bound.

### Attainment

Take `k=q`. Then

\[
{pq\choose q}=p{pq-1\choose q-1}.
\]

Modulo `q`, write

\[
pq-1=(p-1)q+(q-1).
\]

Lucas's theorem gives

\[
{pq-1\choose q-1}
\equiv
{p-1\choose0}{q-1\choose q-1}
\equiv1\pmod q.
\]

Thus `q` does not divide the binomial coefficient, while the prefactor supplies `p`. Hence

\[
\gcd\!\left(pq,{pq\choose q}\right)=p.
\]

Together with the lower bound, `f(pq)=p`.

## Correction history

A later historical registry row attempted to refute the semiprime formula at `n=21` by asserting

`gcd(21, C(21,7)) = 9`.

That statement is arithmetically impossible because `9` does not divide `21`. In fact

\[
{21\choose7}=116280
\]

and

\[
\gcd(21,116280)=3,
\]

exactly as the semiprime theorem predicts.

Other broad characterization attempts in the #700 campaign did fail. This note preserves only the two universal families proved above and does not promote any stronger characterization of general composite `n`.

## Scope

These are exact structural families for Erdős #700, not a resolution of every clause of the parent problem. No historical novelty claim is made for the underlying Lucas/valuation identities.
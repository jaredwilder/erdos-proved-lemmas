# Erdős #700 — exact semiprime binomial-gcd formula

Author: Jared Wilder. Public release: 2026-09-11.

For `n>=2`, define

`f(n)=min_{1<k<=n/2} gcd(n, C(n,k))`.

## Theorem

If `n=pq` with primes `p<=q`, then

`f(pq)=p`.

### Lower bound

From

`k C(n,k) = n C(n-1,k-1)`

one gets

`n / gcd(n,C(n,k)) | k`.

Hence `gcd(n,C(n,k))` cannot be 1 for `1<k<=n/2`. When `n=pq`, every nontrivial divisor of `n` is at least `p`, so

`f(pq)>=p`.

### Matching upper bound

Take `k=q`. Then

`C(pq,q)=p C(pq-1,q-1)`.

Lucas' theorem gives

`C(pq-1,q-1) ≡ 1 (mod q)`,

so `q` does not divide `C(pq,q)`, while `p` does. Therefore

`gcd(pq,C(pq,q))=p`,

and hence `f(pq)=p`.

The square case `p=q` is included by the corresponding elementary p-adic/Lucas calculation.

Checks such as `f(21)=3`, `f(35)=5`, `f(49)=7`, and `f(77)=7` agree with the theorem. The result is exact on the full semiprime class; behavior for integers with three or more prime factors is a separate question.

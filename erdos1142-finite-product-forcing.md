# Erdős #1142 — finite primitive-root product forcing

**Author:** Jared Wilder  
**Release:** 2026-09-11

Let `Good(n)` denote the frozen #1142 property that every admissible difference `n-2^j` with `1<2^j<n` is prime.

## Orbit-avoidance lemma

Let `p` be an odd prime and put

\[
r=\operatorname{ord}_p(2).
\]

If

\[
Good(n),\qquad n>p+2^r,
\]

then either `p|n` or

\[
n\bmod p\notin\langle2\rangle.
\]

### Proof

Suppose `p∤n` and `n mod p` lies in `<2>`. Choose `1<=j<=r` with

\[
n\equiv2^j\pmod p.
\]

Then `p|(n-2^j)`. Also

\[
n-2^j\ge n-2^r>p>1.
\]

Thus `n-2^j` is a multiple of `p` strictly larger than `p`, hence composite, contradicting `Good(n)`.

## Primitive-root corollary

If 2 is a primitive root modulo `p`, then `<2>` is the whole nonzero residue group. Therefore

\[
\boxed{
Good(n),\ n>p+2^{p-1}
\Longrightarrow
p\mid n.
}
\]

## Finite-product forcing theorem

Let `P` be any finite set of odd primes for which 2 is a primitive root. Then

\[
\boxed{
Good(n),\quad
n>\max_{p\in P}(p+2^{p-1})
\Longrightarrow
\prod_{p\in P}p\mid n.
}
\]

Apply the primitive-root corollary to each member of `P`; distinct primes are coprime, so their product divides `n`.

## Exact first towers

| primitive-root primes | strict threshold | forced divisor |
|---|---:|---:|
| `{3,5}` | `21` | `15` |
| `{3,5,11}` | `1035` | `165` |
| `{3,5,11,13}` | `4109` | `2145` |
| `{3,5,11,13,19}` | `262163` | `40755` |

The strict boundary is load-bearing: the estate retains `n=21,p=5` as the exact regression counterexample to an older non-strict formulation.

## Scope boundary

This theorem forces arbitrary **finite** products once a finite list of primitive-root primes is supplied. Passing to an infinite product would require unconditional information about infinitely many primes for which 2 is a primitive root; no form of Artin's conjecture is assumed here.

The parent problem remains separate. This is an exact structural sieve theorem, not a global close.

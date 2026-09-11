# Erdős proved lemmas

**Finished mathematical lemmas extracted from larger Erdős research projects and published as standalone results rather than left buried under the status of the parent problem.**

Author: Jared Wilder. First public timestamp: 2026-09-11.

The current collection includes independently rechecked results on Erdős 978, 126, 1107 and 893, together with structural lemmas or reductions for 396, 373, 602, 774, 1142 and 289. Each entry states exactly what it establishes and what checking has been done.

Four entries were **reverified independently on 2026-09-11** before publication and are marked **[checked]**. The remaining entries preserve their recorded mathematical arguments for direct inspection.

---

## Erdős 978 — `4 ∤ n⁴ + 2` for every integer n **[checked]**

Modulo 16, `n⁴ ≡ 0` for even `n` and `n⁴ ≡ 1` for odd `n`, so `n⁴ + 2 ≡ 2` or `3 (mod 16)`. Neither is divisible by 4.

**Consequence: `n⁴ + 2` is never a fourth power, nor any `4k`-th power, for any integer `n`.**

Verified over `n ∈ [−500,500]`: no `n` with `4 | n⁴+2`.

## Erdős 126 — no three distinct positive integers have all pairwise sums powers of 2 **[checked]**

Suppose `a+b = 2^p`, `a+c = 2^q`, `b+c = 2^r` with `p < q < r`. Then

```text
2a = 2^p + 2^q − 2^r <= 3·2^(q−1) − 2^(q+1) < 0,
```

so no such `a` exists.

Verified exhaustively over all triples `a<b<c<600`.

## Erdős 1107 — 87 is not a sum of at most three squarefull numbers **[checked]**

The complete squarefull basis below 88 is

```text
1, 4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 72, 81.
```

Exhaustive search over sums of at most three of these numbers, with repetition allowed, finds no representation of 87. At `r=2` the conjecture asks for sums of at most `r+1=3`, so **87 is an exception**, extending the recorded gap set to `{7,15,23,87}`.

## Erdős 893 — `τ(2^k − 1) ≥ τ(k)` for every `k ≥ 1` **[checked]**

If `a | k`, then `2^a−1 | 2^k−1` by the geometric-sum identity

```text
2^k − 1 = (2^a − 1) Σ_{i<m} 2^{ia}.
```

The map `a ↦ 2^a−1` is injective, so it embeds the divisors of `k` into the divisors of `2^k−1`.

Verified for all `k<60`.

The same mechanism also gives `τ(2^{2k}−1) ≥ 2τ(2^k−1)`, since `2^{2k}−1=(2^k−1)(2^k+1)` and the two odd factors are coprime.

---

## Erdős 396 — a construction eliminating all small primes simultaneously

Let

```text
M(k) = Π_{p ≤ 2k+1} p^{E_p},
E_p = floor(log_p((k+1)!)) + 1,
```

and impose `n ≡ −1 (mod M(k))`.

For each `p≤2k+1` and `i≤k`, `n−i ≡ −(i+1) (mod p^{E_p})`, so

```text
v_p(Π(n−i)) = v_p((k+1)!) ≤ E_p−1.
```

Meanwhile the low base-`p` digits of `n` are all `p−1`, so adding `n+n` creates carries at every position below `E_p`, giving

```text
v_p(C(2n,n)) ≥ E_p > v_p((k+1)!).
```

A supporting valuation identity is

```text
v_q(C(2n,n)) = floor(2i/q) + v_q(C(2s,s))
```

when `q∤n`, `n=qs+i`, and `0<i<q`.

## Erdős 373 — no solutions when `n−1` is prime

If `p=n−1` is prime and `n≥3`, then

```text
n! = a₁!···a_k!,   n−1 > a₁ ≥ ··· ≥ a_k ≥ 2
```

has no solutions: every `a_i≤n−2=p−1`, so none of the factorials on the right is divisible by `p`, while `p|n!`.

An exhaustive companion search over `2≤n≤36` finds exactly the three known solutions, all with `n−1` composite:

```text
9!  = 7!·3!·3!·2!
10! = 7!·6!
16! = 14!·5!·2!.
```

## Erdős 602 — finite hypergraphs with no one-point edge intersections are 2-colourable

Let `H` be a minimal non-2-colourable finite hypergraph with no two distinct edges meeting in exactly one vertex.

First, `H` is Sperner: if `f⊊e` are edges, a 2-colouring of `H−e` supplied by minimality cannot make `e` monochromatic, because then `f` would already be monochromatic. The single-flip argument then completes the proof; the only obstruction would be a pair of edges meeting in exactly one vertex.

The argument in fact does not need a lower bound on edge size.

## Erdős 774 — dissociated subsets of a dyadic block are logarithmically small

All `2^|D|` subset sums of a dissociated set `D` are distinct, while each is at most `Σ_{d∈D} d ≤ 2N|D|`. Hence

```text
2^|D| ≤ 2N|D| + 1,
```

which gives

```text
|D| ≤ log₂ N + O(log log N).
```

Thus a set containing a dissociated subset of proportional size is extremely sparse inside a dyadic block.

## Erdős 1142 — congruence reduction for Good numbers

Call `n` Good if `n−2^k` is prime for every `1≤2^k<n`. Forced divisibility over primes for which 2 is a primitive root gives:

```text
n > 21      => n ≡ 0,45,75 (mod 105),
n > 262165  => 4849845 | n,
```

with `n mod 23` restricted to a 12-class set.

**Any counterexample beyond 105 must lie in one of exactly 288 residue classes modulo 111,546,435.** This corrects an earlier count of 324.

The even case is complete: `n` even forces `n=2^k+2`, so

```text
Good ∩ 2N = {4}.
```

Exhaustively,

```text
Good ∩ [3,2^20] = {4,7,15,21,45,75,105}.
```

## Erdős 289 — a `p`-adic generalisation of Kürschák's theorem

If `S` is a finite set of integers at least 2 with

```text
Σ_{n∈S} 1/n ∈ Z,
```

then for every prime `p`, writing

```text
A_p = {n/p : n∈S, p|n},
```

we have

```text
v_p(Σ_{m∈A_p} 1/m) ≥ 1.
```

Only multiples of `p` contribute negative `p`-adic valuation; factoring out `1/p` and iterating gives the claim. The case `p=2` is Kürschák's classical theorem. The statement was checked on all 21 integral-reciprocal-sum subsets of `[2,20]`.

This entry has not yet been formalized in Lean.

---

## Verification status

The statements above are lemmas and reductions with their own scopes, regardless of whether the larger Erdős problems in which they arose remain open.

Four entries were independently rechecked for this release. The others are published with their recorded arguments so that those arguments can be checked directly. Claims that later fail are kept in the separate correction record rather than silently mixed into this collection.
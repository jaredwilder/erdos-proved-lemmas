# Erdős proved lemmas

**Finished mathematical lemmas, exact subcases, and structural reductions extracted from larger Erdős research projects.** This repository is the canonical public home for compact proved child results that do not yet justify a larger dedicated subject repository.

Author: Jared Wilder. First public timestamp: 2026-09-11.

A parent Erdős problem may remain open while a theorem proved inside its investigation is complete. Entries here are therefore organized by the statement actually established, not by the status of the larger problem.

## Results

| problem | result | evidence |
|---|---|---|
| **#85** | `f(5)=f(6)=f(7)=3` for the minimum-degree/C4 function | elementary proof + exhaustive graph check |
| **#126** | no three distinct positive integers have all pairwise sums powers of 2 | elementary proof + exhaustive check |
| **#289** | all-prime p-adic obstruction for finite integral reciprocal sums | elementary p-adic proof; finite head/tail lemma separately formalized |
| **#291** | corrected leading-`p` harmonic divisibility criterion using `q=floor(n/p^e)` | analytic proof + finite regression |
| **#313** | for fixed `k`, only finitely many reciprocal-prime solutions exist | elementary finite-branching proof |
| **#373** | no factorial-product solution when `n-1` is prime | elementary divisibility proof |
| **#396** | construction simultaneously eliminating all small primes in the stated binomial-divisibility setting | valuation/carry argument |
| **#602** | finite hypergraphs whose edges all have size at least 2 and with no one-point edge intersections are 2-colourable | minimal-counterexample + single-flip proof; independently rechecked |
| **#700** | for semiprime `n=pq`, `f(pq)=p` for the binomial-gcd function | divisibility identity + Lucas theorem |
| **#774** | dissociated subsets of a dyadic block have logarithmic size | subset-sum counting |
| **#893** | `τ(2^k-1) >= τ(k)` and a doubling consequence | divisor injection; independently checked |
| **#978** | `4 ∤ n^4+2` for every integer `n` | congruence proof; independently checked |
| **#1107** | 87 is not a sum of at most three squarefull numbers | exhaustive finite basis search |
| **#1142** | strong congruence compression for Good numbers, including exactly 288 residue classes modulo 111,546,435 beyond the stated threshold | arithmetic reduction + exhaustive check |

## Full writeups for the newest routed results

- [`erdos85-small-values.md`](erdos85-small-values.md)
- [`erdos289-padic-reciprocal-obstructions.md`](erdos289-padic-reciprocal-obstructions.md)
- [`erdos291-leading-p-harmonic-criterion.md`](erdos291-leading-p-harmonic-criterion.md)
- [`erdos313-fixed-k-finiteness.md`](erdos313-fixed-k-finiteness.md)
- [`erdos700-semiprime-binomial-gcd.md`](erdos700-semiprime-binomial-gcd.md)

The original extraction copies remain in the larger `unpublished-math-papers` archive as provenance. Once a result is routed here, this repository is the preferred reading surface for the theorem.

## Selected older results

### Erdős 126

Suppose `a+b=2^p`, `a+c=2^q`, `b+c=2^r` with `p<q<r`. Then

`2a = 2^p+2^q-2^r < 0`,

contradicting positivity. Hence no three distinct positive integers have all pairwise sums powers of two.

### Erdős 893

If `a|k`, then `2^a-1 | 2^k-1`. The injective map `a -> 2^a-1` therefore sends divisors of `k` to divisors of `2^k-1`, proving

`τ(2^k-1) >= τ(k)`.

The same factorization gives `τ(2^{2k}-1) >= 2τ(2^k-1)`.

### Erdős 978

Modulo 16, `n^4` is 0 or 1, so `n^4+2` is 2 or 3 modulo 16. In particular it is never divisible by 4 and hence cannot be a fourth power or any `4r`-th power.

### Erdős 1107

The squarefull numbers below 88 are

`1,4,8,9,16,25,27,32,36,49,64,72,81`.

Exhaustive search over sums of at most three of them, with repetition, gives no representation of 87.

### Erdős 373

If `p=n-1` is prime, every factorial `a_i!` with `a_i<n-1` is prime to `p`, while `p|n!`. Hence an identity `n!=a_1!...a_k!` with all `a_i<n-1` is impossible.

### Erdős 602

Let `H` be a finite hypergraph in which every edge has at least two vertices and no two distinct edges meet in exactly one vertex. Then `H` is 2-colourable.

Suppose not, and choose a counterexample with the minimum number of edges. Remove an edge `e` and properly 2-colour the remaining hypergraph. If `e` is bichromatic we are done, so assume `e` is all red. Choose `v∈e` and flip only `v` to blue. Since `|e|≥2`, `e` is now bichromatic. If another edge `f` becomes monochromatic, it must become all blue and must contain `v`; before the flip `v` was its unique red vertex. Every other vertex of `e` remains red, so none lies in `f`, giving `e∩f={v}`, contradiction.

The edge-size hypothesis is necessary for the theorem as stated: the one-edge hypergraph `{{v}}` has no pair of distinct edges meeting in one vertex but is not 2-colourable. An earlier release sentence claiming that no lower bound on edge size was needed was too strong and is corrected here. A brute-force regression over all hypergraphs on at most four vertices satisfying the corrected hypotheses found no counterexample; `K_4^3` is also explicitly 2-colourable by a 2–2 split.

### Erdős 774

For a dissociated set `D`, all `2^|D|` subset sums are distinct and at most `2N|D|` in a dyadic block. Thus

`2^|D| <= 2N|D|+1`,

so `|D| <= log_2 N + O(log log N)`.

### Erdős 1142

The released congruence analysis gives

`n>21 => n ≡ 0,45,75 (mod 105)`,

and beyond the stronger threshold every counterexample lies in exactly 288 residue classes modulo 111,546,435. The even case is complete: the only even Good number is 4.

## Verification and corrections

Some entries have independent finite checks, some have formal fragments, and some are ordinary proofs. Each writeup states its own evidence. Historical novelty is a separate literature question.

If a later audit corrects an entry, the correction should be attached to that entry rather than used as a disclaimer for unrelated theorems.

## License

Apache-2.0.

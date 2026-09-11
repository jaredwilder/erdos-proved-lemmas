# Erdős #400 — elementary logarithmic upper bound and factorial subsequence

Author: Jared Wilder  
Public release: 2026-09-11

For fixed `k>=2`, let `g_k(n)` be the maximum of

`a_1+...+a_k-n`

over tuples satisfying

`a_1! ... a_k! | n!`.

## Theorem 1 — elementary pointwise upper bound

For every `n>=1`,

`g_k(n) <= k(floor(log_2 n)+1)`.

### Proof

Any admissible `a_i` satisfies `a_i<=n`, since `a_i!|n!` is impossible for `a_i>n`.

Let `s_2(r)` be the sum of the binary digits of `r`. Legendre's formula gives

`v_2(r!) = r-s_2(r)`.

Divisibility of the factorial product implies

`sum_i (a_i-s_2(a_i)) <= n-s_2(n)`.

Hence

`sum_i a_i - n <= sum_i s_2(a_i)-s_2(n)`

`<= sum_i s_2(a_i)`

`<= k(floor(log_2 n)+1)`.

Taking the maximum over admissible tuples proves the bound.

## Theorem 2 — explicit unbounded factorial subsequence

For every integer `m>=2`, putting `n=m!` gives

`g_k(m!) >= m+k-3`.

### Proof

Choose

`(a_1,...,a_k)=(m!-1,m,1,...,1)`.

Then

`(m!-1)! * m! = (m!)!`,

so the tuple is admissible for the argument `n=m!`. Its excess is

`(m!-1)+m+(k-2)-m! = m+k-3`.

## Literature boundary

The logarithmic pointwise order is classical: Erdős and Graham explicitly record that `g_k(n) <<_k log n` is easy. A 2026 paper of Eric Li gives a sharper pointwise upper bound and a density-one logarithmic lower bound. This note makes **no historical novelty claim** for Theorem 1.

The purpose of this release is to preserve the exact elementary digit-sum derivation recovered in the Day-One estate and the explicit factorial subsequence in one auditable place.

The two asymptotic questions in Erdős #400 remain the parent problem.

## License

Apache-2.0.

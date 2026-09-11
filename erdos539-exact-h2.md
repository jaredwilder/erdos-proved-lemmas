# Erdős #539 — exact base case `h(2)=2`

Author: Jared Wilder. Public release: 2026-09-11.

For a finite set `A⊂N`, define

`Q(A) = { a/gcd(a,b) : a,b∈A }`.

Let `h(n)` be the largest integer such that every `n`-element set `A⊂N` satisfies `|Q(A)|>=h(n)`.

## Theorem

`h(2)=2`.

## Proof

Take any two-element set

`A={a,b}`, `a!=b`,

and put `g=gcd(a,b)`.

The four ordered choices of `(a,b)` in the definition produce

`Q(A)={1,a/g,b/g}`.

The two numbers `a/g` and `b/g` are distinct, so `|Q(A)|>=2` for every two-element set.

This lower bound is attained. For example, with

`A={1,2}`,

one has

`Q(A)={1,2}`.

Therefore `h(2)=2`.

## Scope

This is an exact base case only. The asymptotic estimation of `h(n)` is a substantially deeper problem.

Historical novelty is not claimed.
# Exact Sidon optimum on `Fin 8`

Author: Jared Wilder. Public release: 2026-09-11.

## Theorem

Under the Sidon convention that all unordered pair sums with repetition must be distinct, the largest Sidon subset of

`{0,1,2,3,4,5,6,7}`

has size exactly `4`.

## Lower bound

The set

`{0,1,3,7}`

is Sidon. Its unordered pair sums with repetition are

`0,1,2,3,4,6,7,8,10,14`,

which are all distinct.

Hence the optimum is at least `4`.

## Upper bound

The recovered formal certificate exhaustively checks all 5-element subsets of `Fin 8` and proves that each contains a nontrivial equal pair-sum. Therefore no 5-element Sidon subset exists.

Hence the exact optimum is

`4`.

## Evidence boundary

The lower witness is elementary and directly inspectable. The upper bound is a finite exhaustive theorem previously kernel-checked in the recovered estate; this note does not promote that finite certificate into any larger asymptotic Sidon claim.

Historical novelty is not claimed.
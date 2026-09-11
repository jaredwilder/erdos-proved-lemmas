# Erdős #276 — common divisors of a Fibonacci-type recurrence

Author: Jared Wilder  
Public release: 2026-09-11

Let `a_0,a_1,...` be an integer sequence satisfying

`a_(n+2)=a_(n+1)+a_n`.

## Theorem

For every positive integer `d`,

`d` divides every term of the sequence if and only if `d` divides both `a_0` and `a_1`.

Equivalently, the greatest common divisor of all terms is

`gcd(a_0,a_1)`.

## Proof

Any common divisor of all terms certainly divides the first two terms.

Conversely, if `d|a_0` and `d|a_1`, induction through the recurrence gives `d|a_n` for every `n`.

Thus the common-divisor condition in Erdős #276 is exactly a condition on the seed pair. In particular, coprime seeds automatically satisfy the requirement that no integer greater than 1 divide every term.

## Scope

This resolves the common-divisor clause only. The difficult part of Erdős #276 is constructing coprime seeds whose entire recurrence consists of composite numbers.

## License

Apache-2.0.

# Erdős #829 — divisor bound for representations as two positive cubes

**Author:** Jared Wilder  
**Public routing:** 2026-09-11  
**Source:** Pass-3 promoted theorem, independently rechecked

For `n>=1`, let

\[
r_3(n)=\#\{(x,y)\in\mathbb Z_{>0}^2:x^3+y^3=n\},
\]

counting ordered representations.

## Theorem

For every positive integer `n`,

\[
\boxed{r_3(n)\le 2\tau(n).}
\]

## Proof

From

\[
x^3+y^3=(x+y)(x^2-xy+y^2)=n,
\]

put

\[
d=x+y.
\]

Then `d|n`. Once `d` is fixed, write `s=xy`. Since

\[
x^2-xy+y^2=(x+y)^2-3xy=d^2-3s,
\]

we have

\[
\frac nd=d^2-3s,
\]

and hence

\[
\boxed{s=\frac{d^2-n/d}{3}.}
\]

Thus both the sum `x+y=d` and product `xy=s` are fixed by the divisor `d`. The numbers `x,y` are roots of

\[
T^2-dT+s=0,
\]

so for each divisor `d` there are at most two ordered pairs `(x,y)`. Summing over the at most `tau(n)` positive divisors gives

\[
r_3(n)\le2\tau(n).
\]

## Scope

This is an exact universal divisor bound. It does not by itself prove a uniform polylogarithmic representation bound: the maximal order of `tau(n)` is larger than every fixed power of `log n`. Historical routes that treated this estimate as a parent-problem close are therefore not promoted.

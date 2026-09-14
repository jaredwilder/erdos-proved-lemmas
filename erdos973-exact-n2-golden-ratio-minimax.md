# Erdős #973 — exact n=2 golden-ratio minimax

**Author:** Jared Wilder  
**Public release:** 2026-09-14

## Theorem

For

\[
M_2:=\min_{|z|\ge1}\max\bigl(|1+z^2|,|1+z^3|\bigr),
\]

one has

\[
\boxed{
M_2=2\cos\frac{2\pi}{5}=\frac{\sqrt5-1}{2}.
}
\]

Equality is attained at

\[
z=e^{2\pi i/5}
\]

(and by the symmetric conjugate choice).

## Step 1 — radial reduction is exact

Write

\[
z=re^{i\theta},\qquad r\ge1.
\]

For `k=2,3`, put `t=r^k>=1`. Then

\[
|1+r^ke^{ik\theta}|^2
=1+t^2+2t\cos(k\theta).
\]

As a function of `t`, the derivative is

\[
2(t+\cos(k\theta))\ge0
\]

because `t>=1` and `cos(k theta)>=-1`.

Thus each of the two moduli is nondecreasing as `r` moves outward from `1`. Hence the minimax is attained on the unit circle:

\[
M_2=\min_{\theta\in\mathbb R}
\max\left(2|\cos\theta|,2\left|\cos\frac{3\theta}{2}\right|\right).
\]

## Step 2 — exact angular lower bound

Let

\[
a=\cos\frac{2\pi}{5}=\sin\frac{\pi}{10}.
\]

For any real `u`,

\[
|\cos u|<a
\]

holds exactly when, modulo `pi`,

\[
u\in\left(\frac{2\pi}{5},\frac{3\pi}{5}\right).
\]

Suppose both terms in the maximum were strictly below `2a`. Then simultaneously

\[
\theta\pmod\pi\in
\left(\frac{2\pi}{5},\frac{3\pi}{5}\right)
\]

and

\[
\frac{3\theta}{2}\pmod\pi\in
\left(\frac{2\pi}{5},\frac{3\pi}{5}\right).
\]

On `theta in [0,2pi)`, the first condition gives the two intervals

\[
\left(\frac{2\pi}{5},\frac{3\pi}{5}\right),\qquad
\left(\frac{7\pi}{5},\frac{8\pi}{5}\right).
\]

The second condition pulls back to

\[
\left(\frac{4\pi}{15},\frac{2\pi}{5}\right),
\quad
\left(\frac{14\pi}{15},\frac{16\pi}{15}\right),
\quad
\left(\frac{8\pi}{5},\frac{26\pi}{15}\right).
\]

These open interval families are disjoint. They touch only at the boundary values `theta=2pi/5` and its symmetric translates. Therefore

\[
\max\left(|\cos\theta|,\left|\cos\frac{3\theta}{2}\right|\right)
\ge a.
\]

Hence

\[
M_2\ge2a.
\]

At `theta=2pi/5`,

\[
|\cos\theta|
=\left|\cos\frac{3\theta}{2}\right|
=\cos\frac{2\pi}{5},
\]

so equality holds.

Finally,

\[
2\cos\frac{2\pi}{5}=\frac{\sqrt5-1}{2}.
\]

## Correction history

An earlier campaign route recorded a conflicting symbolic value for an `n=2` quantity after an incompletely justified radial reduction. That sibling value is not used here. The later R008 route supplied the correct coupled-same-witness minimax and the radial argument above independently verifies it.

## Scope

This is an exact endpoint theorem for `n=2`. It does not by itself decide the full Erdős #973 problem or transfer to general `n`. Targeted estate searches found no exact prior match for this endpoint calculation; no historical novelty claim is made.
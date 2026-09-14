# Erdős #973 — exact `n=2` golden-ratio minimax

**Author:** Jared Wilder  
**Status:** exact finite subproblem / parent later overtaken externally  
**Novelty:** not asserted here

The recovered estate isolates the exact `n=2` minimax problem

\[
\inf_{|z|\ge1}
\max\bigl(|1+z^2|,|1+z^3|\bigr).
\]

The value is

\[
\boxed{
\inf_{|z|\ge1}
\max\bigl(|1+z^2|,|1+z^3|\bigr)
=
\frac{\sqrt5-1}{2}.
}
\]

This note gives a compact analytic proof of the recovered theorem. It is a standalone exact finite extremum, not a claim about the later externally resolved parent problem.

## 1. Radial reduction

Write

\[
z=re^{i\theta},\qquad r\ge1.
\]

For `k=2,3`,

\[
|1+r^ke^{ik\theta}|^2
=
1+r^{2k}+2r^k\cos(k\theta).
\]

Differentiating in `r` gives

\[
2kr^{k-1}\bigl(r^k+\cos(k\theta)\bigr)\ge0
\qquad(r\ge1),
\]

because `r^k≥1` and `cos(kθ)≥-1`.

Thus both terms are nondecreasing along every ray, so the minimax is attained on the unit circle:

\[
\inf_{|z|\ge1}\max(|1+z^2|,|1+z^3|)
=
\min_{\theta}\max(|1+e^{2i\theta}|,|1+e^{3i\theta}|).
\]

Put `u=θ/2`. Then

\[
|1+e^{2i\theta}|=2|\cos 2u|,
\qquad
|1+e^{3i\theta}|=2|\cos 3u|.
\]

So it remains to prove

\[
\min_u\max(|\cos2u|,|\cos3u|)
=
\frac{\sqrt5-1}{4}.
\]

## 2. Lower bound

Set

\[
c=\frac{\sqrt5-1}{4}=\cos\frac{2\pi}{5}
\]

and

\[
t=\cos^2u\in[0,1].
\]

Then

\[
|\cos2u|=|2t-1|,
\]

and

\[
|\cos3u|
=\sqrt t\,|4t-3|.
\]

Define

\[
t_0=\frac{5-\sqrt5}{8},
\qquad
t_1=\frac{3+\sqrt5}{8}=\cos^2\frac\pi5.
\]

These satisfy

\[
1-2t_0=c,
\qquad
2t_1-1=c,
\qquad
\frac14<t_0<t_1<\frac34.
\]

Now split into three cases.

### Case 1: `t≤t_0`

Then

\[
|2t-1|=1-2t\ge1-2t_0=c.
\]

### Case 2: `t≥t_1`

Then

\[
|2t-1|\ge2t_1-1=c.
\]

### Case 3: `t_0≤t≤t_1`

Here `t>1/4` and `t<3/4`, so

\[
|\cos3u|=\sqrt t(3-4t).
\]

The function

\[
f(t)=\sqrt t(3-4t)
\]

has derivative

\[
f'(t)=\frac{3-12t}{2\sqrt t}<0
\qquad(t>1/4).
\]

Hence on `[t_0,t_1]`,

\[
|\cos3u|=f(t)\ge f(t_1).
\]

Since `t_1=cos^2(π/5)`,

\[
f(t_1)
=|\cos(3\pi/5)|
=\cos(2\pi/5)
=c.
\]

Therefore in every case

\[
\max(|\cos2u|,|\cos3u|)\ge c.
\]

## 3. Equality

Take

\[
u=\frac\pi5,
\qquad
\theta=\frac{2\pi}{5},
\qquad
z=e^{2\pi i/5}.
\]

Then

\[
|\cos2u|
=
|\cos(2\pi/5)|
=c,
\]

and

\[
|\cos3u|
=
|\cos(3\pi/5)|
=c.
\]

Thus

\[
\max(|1+z^2|,|1+z^3|)=2c
=
\boxed{\frac{\sqrt5-1}{2}}.
\]

Together with the lower bound, this proves the theorem.

## Scope / provenance boundary

The estate's final court retained this as a clean exact `n=2` subproblem even though the parent problem was later overtaken by external work. The recovered formalization handoff supplied the frozen target, radial-reduction spine, and `u=π/5` minimizer; this page records a complete compact analytic derivation.

No historical-priority claim is made from the absence of a direct match in the estate's targeted search.

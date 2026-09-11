# Erdős #973 — exact two-point golden-ratio extremum

**Author:** Jared Wilder  
**Public routing:** 2026-09-11

After normalization `z_1=1`, consider

\[
\inf_{|z|\ge1}\max\bigl(|1+z^2|,|1+z^3|\bigr).
\]

## Theorem

\[
\boxed{
\inf_{|z|\ge1}\max\bigl(|1+z^2|,|1+z^3|\bigr)
=\frac{\sqrt5-1}{2}
=2\cos\frac{2\pi}{5}.
}
\]

The optimum is attained at

\[
z=e^{\pm2\pi i/5}.
\]

## Proof capsule

The recovered analytic proof reduces radially to `|z|=1`. Write `z=e^{2iu}`. Then

\[
|1+z^2|=2|\cos2u|,
\qquad
|1+z^3|=2|\cos3u|.
\]

So the minimax becomes

\[
2\min_u\max(|\cos2u|,|\cos3u|).
\]

At the optimum the two active terms balance. The balance occurs at `u=pi/5`, equivalently `z=e^{2pi i/5}`, and

\[
2|\cos(2\pi/5)|=\frac{\sqrt5-1}{2}.
\]

The source campaign separately checked the witness in exact algebra and recorded the one-dimensional lower-bound/equalization argument as the symbolic optimality proof.

## Scope and novelty

This is an exact finite-dimensional extremum, not a solution of the historical parent problem. The 2026 audit reports that the parent problem was subsequently solved negatively by external work.

Targeted literature checks in that audit did not locate an explicit `n=2` golden-ratio evaluation, so the estate labels this **plausibly original exact finite extremum**, not a definitive historical-priority certificate.

The full extraction remains archived in `unpublished-math-papers/erdos973-two-point-extremum/`.

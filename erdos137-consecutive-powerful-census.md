# Erdős #137 — corrected census of consecutive powerful integers through 300,000

**Author:** Jared Wilder  
**Status:** exact finite census / correction  
**Parent problem:** not claimed resolved

A positive integer is **powerful** if every prime dividing it occurs to exponent at least 2.

A historical transcript listed nine starts of pairs of consecutive powerful integers below 300,000:

`{8,288,675,1444,1681,2312,4624,6724,9800}`.

Five entries are false because the successor is not powerful. A fresh exact factorization sieve gives the corrected set

\[
\boxed{\{8,288,675,9800,12167,235224\}}.
\]

Thus, for `2 <= n < 300000`, the powerful pairs `(n,n+1)` are exactly

- `(8,9)`;
- `(288,289)`;
- `(675,676)`;
- `(9800,9801)`;
- `(12167,12168)`;
- `(235224,235225)`.

For example,

- `288 = 2^5*3^2`, `289 = 17^2`;
- `675 = 3^3*5^2`, `676 = 2^2*13^2`.

## No triple in the same range

The same exhaustive sieve finds

\[
\boxed{\text{no }n<300000\text{ for which }n,n+1,n+2\text{ are all powerful}.}
\]

This is a bounded statement only.

## What was wrong in the old list

The starts

`1444,1681,2312,4624,6724`

fail because respectively

`1445,1682,2313,4625,6725`

are not powerful.

The old list also omitted the genuine starts `12167` and `235224`.

## Scope and provenance

Recovered from the raw-session transcript audit and independently recomputed again before this publication. This note records an exact finite census and correction; it does not extrapolate the bounded computation into a global theorem about consecutive powerful numbers.

Historical novelty is not claimed.

# Erdős #978 — fourth-power and mod-9 congruence sieves

Author: Jared Wilder. Public release: 2026-09-11.

## Theorem 1 — fourth-power obstruction

For every integer `n`,

`4 ∤ n^4+2`.

Consequently `n^4+2` is never a fourth power, nor any perfect `4r`-th power.

### Proof

Modulo 4, every fourth power is `0` or `1`. Hence

`n^4+2 ≡ 2 or 3 (mod 4)`.

So the number is not divisible by 4, whereas every positive fourth power greater than 1 that is even is divisible by 16, and an odd fourth power is 1 modulo 4. Either way equality is impossible.

## Theorem 2 — exact divisibility by 9

For every integer `n`,

`9 | n^4+2`

if and only if

`n≡2 or 7 (mod 9)`.

### Proof

Checking the nine residue classes modulo 9, the fourth-power residues are

- `0` when `n≡0,3,6`;
- `1` when `n≡1,8`;
- `4` when `n≡4,5`;
- `7` when `n≡2,7`.

Thus `n^4+2≡0 (mod 9)` exactly in the final pair of classes.

## Scope

These are exact congruence obstructions/sieves. They do not classify the full factorization or perfect-power behavior of `n^4+2` beyond the stated consequences.

Historical novelty is not claimed.
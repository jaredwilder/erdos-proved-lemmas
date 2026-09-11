# Erdős #197 — every finite set admits a beautiful ordering

**Author:** Jared Wilder  
**Public routing:** 2026-09-11

## Theorem

Every finite set `S⊂N` admits an ordering `x_1,...,x_m` with no indices `i<j<k` satisfying

\[
x_i+x_k=2x_j.
\]

## Proof by parity recursion

Induct on `|S|`. Split `S` into odd and even elements. Put the odd block first and the even block second. Normalize the odd block by `x↦(x-1)/2` and the even block by `x↦x/2`, recursively choose beautiful orderings of the two smaller normalized sets, and lift them back.

If a forbidden ordered three-term progression existed in the concatenated ordering, its two endpoints would have the same parity because `x_i+x_k=2x_j` is even. Thus both endpoints lie in the same contiguous parity block, and so does the middle indexed term. Dividing by 2 after parity normalization produces a forbidden progression in the corresponding recursively ordered smaller set, contradiction.

## Scope

This closes the finite analogue only. The infinite ordering / order-type problem remains separate. The mechanism is classical in flavor and no historical novelty claim is made.

The original extraction remains archived in `unpublished-math-papers/erdos197-finite-beautiful-ordering/`.

# Computer Science worked-example guidance

## Source pattern

SimpleStudy separates concepts into compact sections with frequent note callouts. Programming
material must add executable examples and tests. SEC assessment requirements control the response;
all tasks and code must be original.

## Required answer shape

1. State inputs, output, constraints and edge cases.
2. Describe the algorithm before implementation.
3. Use clear names and the assessed language where required.
4. Trace or test normal, boundary and invalid cases.
5. Evaluate correctness, efficiency and limitations.

## Original model

**Synthetic prompt:** Return the largest value in a non-empty list without using `max`.

**Model shape:** Initialise `largest` from the first item, compare each remaining item and replace
`largest` only when a greater value is found. Test a one-item list, all-negative values, repeated
maximum values and a typical mixed list. State that an empty list must be rejected or handled by a
specified contract.

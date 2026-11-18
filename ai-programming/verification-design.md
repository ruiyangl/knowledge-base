# Verification Design

## Resources
[Agentic Verification (Addy Osmani)](https://addyo.substack.com/p/agentic-verification)


## Osmani Notes
- Write end-to-end tests that simulate real user flows and act as the ground truth
- Use property-based testing to specify what should never happen and generate thousands of test cases that attempt to break those constraints
- If replacing a system, compare the old and new versions using randomly selected inputs
- Require tests to run quickly and deterministically, which reinforces the agent to retry when the loop is slow or unreliable (the agent may learn to retry, not fix the problem)

### E2E test

### Property-tests
- Tools 
  - fast-check for JS/TS
  - Hypothesis for Python
  - proptest for Rust
- Testing ideas
  - Round-trip encoding: the value I encode and then decode is the same as the one I started with. Parsing and serializing a value yields the value I started with.
  - Invariants: sorting doesn’t change the number of elements or the contents of the collection. A balance never becomes a negative number. Money in is money out.
  - Idempotency: migrating, normalizing, or retrying the same thing twice has the same effect as doing it once.
  - Equivalence: the optimized function yields the same result as the simple, correct one.

### Unit test and other CI tests
- Make the loop fast and deterministic
- fast enough for each cycle
- same result everytime
- flaky tests quarantined
- short specific failures
- quick loop first by AI automatically, heavy lifting latter

### Write the check before the code
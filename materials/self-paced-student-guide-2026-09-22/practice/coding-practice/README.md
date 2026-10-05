# Practice cost calculator

This is a classroom prototype with one deliberate calculation mistake.
It does not use a network, accounts, payments, or real financial information.

Open `index.html` in a browser. Try a quantity and the cost of one item.

For Task 22, ask the agent to read `calculator.js` and `tests.cjs`, explain
the tests, and run `node tests.cjs` in this folder. Node.js must already be
available, or be installed through your approved software route.

The starting code passes the whole-number and invalid-input checks but fails
the two decimal-price checks. This is intentional. Don't weaken the tests.

Your task is to fix decimal-price calculations without breaking the other
behaviour. Keep a recoverable copy before making changes. Ask your agent to
work within a short limit, then inspect the change and run the tests again.

Files it may change for the first repair: `calculator.js` only.
Files it must not change without a new decision: `tests.cjs`, `index.html`.

Try another input yourself after the supplied tests pass.

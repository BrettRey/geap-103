const assert = require('node:assert/strict');
const { totalCost } = require('./calculator.js');
const cases = [
  ['whole-number price: 2 × 3 = 6', () => assert.equal(totalCost(2, 3), 6)],
  ['decimal price: 3 × 2.50 = 7.50', () => assert.equal(totalCost(3, 2.50), 7.50)],
  ['decimal price: 4 × 1.25 = 5.00', () => assert.equal(totalCost(4, 1.25), 5)],
  ['a blank price needs an error', () => assert.throws(() => totalCost(2, ''), /Enter/)],
  ['a negative quantity needs an error', () => assert.throws(() => totalCost(-1, 2), /Quantity/)],
  ['a word instead of a quantity needs an error', () => assert.throws(() => totalCost('two', 2), /Quantity/)],
];
let passed = 0;
for (const [name, run] of cases) {
  try { run(); passed++; console.log(`PASS: ${name}`); }
  catch (error) { console.log(`FAIL: ${name}\n${error.message}`); }
}
console.log(`${passed} passed; ${cases.length - passed} failed.`);
process.exitCode = passed === cases.length ? 0 : 1;

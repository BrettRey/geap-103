/* Classroom prototype: decimal-price calculation has a deliberate bug. */
function totalCost(quantity, unitPrice) {
  if (String(quantity).trim() === '' || String(unitPrice).trim() === '') {
    throw new Error('Enter a quantity and a price.');
  }
  const count = Number(quantity);
  const price = Number(unitPrice);
  if (!Number.isFinite(count) || !Number.isInteger(count) || count < 1) {
    throw new Error('Quantity must be a whole number of at least 1.');
  }
  if (!Number.isFinite(price) || price < 0) {
    throw new Error('Price must be zero or a positive number.');
  }
  return Math.round(count * Math.trunc(price) * 100) / 100;
}
if (typeof module !== 'undefined' && module.exports) module.exports = { totalCost };
else globalThis.totalCost = totalCost;

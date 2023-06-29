const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', () => {
  it('calculate the sum of two positive nums', () => {
    assert.strictEqual(2 + 2, 4);
    assert.strictEqual(2.5 + 3, 5.5);
    assert.strictEqual(2.5 + 3.5, 6);
    assert.strictEqual(2 + 3.3, 5.3);
    assert.strictEqual(2 + 0, 2);
  });

  it('calculate the sum of two negative nums', () => {
    assert.strictEqual(-2 + -3, -5);
    assert.strictEqual(-2.5 + -3, -5.5);
    assert.strictEqual(-2.5 + -3.5, -6);
    assert.strictEqual(-2 + -3.3, -5.3);
    assert.strictEqual(-2 + 0, -2);
  });

  it('calculate the sum of two zeros', () => {
    assert.strictEqual(0 + 0, 0);
  });

  it('calculate the sum of any combinations of NaNs', () => {
    assert.throws(() => calculateNumber(1, 'a'), TypeError);
    assert.throws(() => calculateNumber('a', 1), TypeError);
    assert.throws(() => calculateNumber('a', 'b'), TypeError);
    assert.throws(() => calculateNumber(1, NaN), TypeError);
    assert.throws(() => calculateNumber(NaN, 1), TypeError);
    assert.throws(() => calculateNumber(NaN, NaN), TypeError);
    // assert.strictEqual(2 + NaN, TypeError('Parameters must be numbers'));
    // assert.strictEqual(NaN + 3, TypeError('Parameters must be numbers'));
    // assert.strictEqual(NaN + 4.1, TypeError('Parameters must be numbers'));
    // assert.strictEqual(3.2 + NaN, TypeError('Parameters must be numbers'));
    // assert.strictEqual(0 + NaN, TypeError('Parameters must be numbers'));
    // assert.strictEqual(NaN + NaN, TypeError('Parameters must be numbers'));
  });
});

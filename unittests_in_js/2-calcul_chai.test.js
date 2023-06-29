const { assert } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', () => {
  it('taking positive numbers', () => {
    assert.equal(calculateNumber('SUM', 1, 3), 4);
    assert.equal(calculateNumber('SUBTRACT', 1, 3), -2);
    assert.approximately(calculateNumber('DIVIDE', 1, 3), 0.3333333333333333, 0.00000001);
  });
  
  it('taking negative numbers', () => {
    assert.equal(calculateNumber('SUM', -1, -3), -4);
    assert.equal(calculateNumber('SUBTRACT', -1, -3), 2);
    assert.approximately(calculateNumber('DIVIDE', -1, -3), 0.3333333333333333, 0.00000001);
  });

  it('taking positive and negative numbers', () => {
    assert.equal(calculateNumber('SUM', -1, 3), 2);
    assert.equal(calculateNumber('SUBTRACT', -1, 3), -4);
    assert.approximately(calculateNumber('DIVIDE', -1, 3), -0.3333333333333333, 0.00000001);
  });

  it('taking zeros', () => {
    assert.equal(calculateNumber('SUM', 0, 0), 0);
    assert.equal(calculateNumber('SUBTRACT', 0, 0), 0);
    assert.equal(calculateNumber('DIVIDE', 0, 0), 'Error');
  });
});
